from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)  # Category ka naam
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name
            

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_as_author')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="postcategory", blank=True, null=True)
    taguser = models.ManyToManyField('auth.User', related_name='tagged_posts', blank=True)
    title = models.CharField(max_length=200)
    image = models.FileField(blank=True, null=True)
    thambelimage= models.FileField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)  # Nullable field
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tags(models.Model):
    taguser=models.ManyToManyField(User)
    posttag=models.ManyToManyField(Post, related_name="post_tags",blank=True, )
    tag_name=models.CharField(max_length=20 )
    
    
    def __str__(self):
        return self.tag_name
