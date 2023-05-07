from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=20)
  content = models.TextField(blank=True)
  photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%M/%D')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_absoulute_url(self):
    return reverse('instagram:post_detail', args=[self.pk])