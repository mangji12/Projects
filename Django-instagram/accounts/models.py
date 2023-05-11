from django.db import models
# User 모델 적용 시 필히 적용시여야 할 라이브러리
# Create your models here.
class User(AbstractUser):
  website_url = models.URLField(blank=True)
  bio - models.TextField(blank=True)

# 커스텀을 위한다면 프로필을 만들어서 할 수도 있긴하다.
# class Profile(models.Model):
#   pass