from django.urls import path

from instagram import views
app_name = 'instagram'
urlpatterns = [
  path('post_form/', views.Post_form, name='post_form'),
  path('<int:pk>/', views.post_detail, name='post_detail'),
  path('post_list/',views.post_list, name='post_list'),
  # path('home/',views.home,name='home')
]