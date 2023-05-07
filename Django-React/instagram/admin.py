from django.contrib import admin

from instagram import models


# Register your models here.
@admin.register(models.Post)
class Post(admin.ModelAdmin):
  list_display = ['author','title','content']