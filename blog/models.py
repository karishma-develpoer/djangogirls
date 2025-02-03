from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)  # Category ka naam
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name

class Post(models.Model):
  

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="postcategory",blank=True, null=True)

    title = models.CharField(max_length=200)
  

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
