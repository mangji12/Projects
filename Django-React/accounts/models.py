from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  photo = models.ImageField(blank=True, upload_to='profile/')