from django.urls import path

from instagram import views

urlpatterns = [
  path('post/', views.post_list)
]