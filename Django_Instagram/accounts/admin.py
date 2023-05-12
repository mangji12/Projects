from django.contrib import admin
from accounts.models import User


# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
  list_display = ['website_url','bio']