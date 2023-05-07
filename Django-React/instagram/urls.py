from django.urls import path

from instagram import views

urlpatterns = [
  path('post_new/', views.Post_new,name='post_new'),
  path('post_detail/<int:pk>/', views.post_detail, name='post_list'),
  path('post_list/',views.post_list,name='post_detail'),
  # path('home/',views.home,name='home')
]