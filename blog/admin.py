from django.contrib import admin
from .models import Post, Category, Tags

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'created_date')
    list_filter = ('author', 'category', 'published_date', 'created_date')
    search_fields = ('title', 'text', 'category__name')  # Search by category name
    list_editable = ('category',)
    ordering = ('-created_date',)
    date_hierarchy = 'created_date'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # List view me category ka naam aur description dikhana
    list_filter = ('name',)  # Filter by category name
    search_fields = ('name',)  # Search by category name

class TagsAdmin(admin.ModelAdmin):
    list_display = ('taguser_list', 'posttag_list', 'tag_name')  # Use custom methods to show related fields
    list_filter = ('taguser', 'posttag', 'tag_name')
    search_fields = ('taguser__username', 'tag_name')  # Search by taguser and tag_name

    # Custom method to display related users (Many-to-Many field 'taguser')
    def taguser_list(self, obj):
        return ", ".join([user.username for user in obj.taguser.all()])  # Display usernames
    taguser_list.short_description = 'Tagged Users'  # Display name in admin panel
    
    # Custom method to display related posts (Many-to-Many field 'posttag')
    def posttag_list(self, obj):
        return ", ".join([post.title for post in obj.posttag.all()])  # Display post titles
    posttag_list.short_description = 'Tagged Posts'  # Display name in admin panel

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)

# Register your models here.
admin.site.site_title = "Blog Post Application"
admin.site.site_header = "Blog Administration"
admin.site.index_title = "Blog administration"
