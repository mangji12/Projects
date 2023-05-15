import tag as tag
from django.db import models
from django.conf import settings
import re

from django.urls import reverse


# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='instagram/post')
  caption = models.CharField(max_length=500)
  # 장고 - taggit을 사용하여 제작할 수 도 있다.
  tag_set = models.ManyToManyField('Tag',blank=True)
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.author

  def extract_tag_list(self):
    tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.caption)
    tag_list = []
    for tag_name in tag_name_list:
      # get_or_create() 메서드는 두 개의 값을 반환합니다. 첫 번째 값은 검색된 또는 생성된 객체이고, 두 번째 값은 불리언(Boolean) 값으로, 해당 객체가 새로 생성되었는지 여부를 나타냅니다.
      tag, _ = Tag.objects.get_or_create(name=tag_name)
      tag_list.append(tag)
    return tag_list

  def get_absolute_url(self):
    return reverse('instagram:post_detail', kwargs={'pk':self.pk}) # args=[self.pk] 도 가능

class Tag(models.Model):
  # unique=True는 해당 필드에 저장되는 값이 고유하다는 것을 보장. 즉, 동일한 name 값을 가지는 두 개의 Tag 인스턴스를 생성할 수 없음.
  # 이는 데이터베이스에서 중복된 값을 방지하는데 사용.
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

