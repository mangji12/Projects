from django.contrib import admin

from instagram.models import Post


# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
  list_display = ['author','title','content']