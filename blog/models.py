from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    #category = models.ForeignKey(Category)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    #author = models.ForeignKey(User)
    author = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})