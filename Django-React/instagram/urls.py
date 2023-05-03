from django.urls import path

from instagram import views

urlpatterns = [
  path('<int:pk>/', views.post_list)
]