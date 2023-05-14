from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

  class GenderChoices(models.TextChoices):
    MALE = 'M', '남성'
    FEMALE = 'F', '여성'

  website_url = models.URLField(blank=True)
  bio = models.TextField(blank=True)
  gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
  profile = models.ImageField(blank=True,upload_to='profile')