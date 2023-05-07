from django.urls import path

from instagram import views

urlpatterns = [
  path('post_new/', views.Post_new),
  path('post_list/<int:pk>/', views.post)
]