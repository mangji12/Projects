from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import resolve_url


# Create your models here.
class User(AbstractUser):
  class GenderChoices(models.TextChoices):
    MALE = 'M', '남성'
    FEMALE = 'F', '여성'

  # 단방향으로 관계를 설정.
  follower_set = models.ManyToManyField('self',blank=True,related_name='following_set',symmetrical=False)

  website_url = models.URLField(blank=True)
  bio = models.TextField(blank=True)
  gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
  profile = models.ImageField(blank=True,upload_to='profile')

  @property
  def profile_url(self):
    if self.profile:
      return self.profile.url
    else:
      return resolve_url("pydenticon_image")