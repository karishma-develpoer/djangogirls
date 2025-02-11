from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponse
import tablib  # डेटा एक्सपोर्ट करने के लिए
from .models import Post, Category, Tags
from import_export.admin import ExportMixin
from import_export.resources import ModelResource

# 📌 User Model Export करने के लिए Resource क्लास बनाएं
class UserResource(ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'is_staff')

# 📌 Export as Excel का Admin Action बनाएँ
def export_as_excel(modeladmin, request, queryset):
    resource = modeladmin.resource_class()
    dataset = resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'
    return response

export_as_excel.short_description = "Download as Excel"


class PostAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ModelResource  
    list_display = ('title', 'author', 'category', 'published_date', 'created_date')
    list_filter = ('author', 'category', 'published_date', 'created_date')
    search_fields = ('title', 'text', 'category__name')
    actions = [export_as_excel]  # Action Dropdown में ऐड करें

# 📌 CategoryAdmin को Update करें
class CategoryAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ModelResource
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    actions = [export_as_excel]

# 📌 TagsAdmin को Update करें
class TagsAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ModelResource
    list_display = ('tag_name',)
    list_filter = ('tag_name',)
    search_fields = ('tag_name',)
    actions = [export_as_excel]

# 📌 UserAdmin को Update करें
class UserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'username', 'email', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')
    actions = [export_as_excel]

# 📌 Models को Register करें
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)

admin.site.site_title = "Blog Post Application"
admin.site.site_header = "Blog Administration"
admin.site.index_title = "Blog administration"