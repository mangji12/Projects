from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=20)
  photo = models.ImageField(blank=True, upload_to='instagram/post')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"작성자 : {self.author}"