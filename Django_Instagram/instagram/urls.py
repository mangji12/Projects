from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator
from instagram import views

app_name = 'instagram'

urlpatterns = [
  path('post/new/',views.post_new,name='post_new'),
  path('post/<int:pk>/',views.post_detail,name='post_detail'),
  re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
  path('post/<int:pk>/like', views.post_like, name='post_like'),
  path('post/<int:pk>/unlike', views.post_unlike, name='post_like'),
  path('',views.index,name='index')
]