from django.db import models
from django import forms

# Create your models here.
class None_item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)
    body = models.TextField()
    #date = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=None, default=None)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20] + '...'