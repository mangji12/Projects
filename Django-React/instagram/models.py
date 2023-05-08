from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=20)
  content = models.TextField(blank=True)
  photo = models.ImageField(blank=True, upload_to='instagram/post/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def get_absolute_url(self):
    return reverse('instagram:post_detail', args=[self.pk])