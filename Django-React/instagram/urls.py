from django.urls import path

from instagram import views
app_name = 'instagram'
urlpatterns = [
  path('post_new/', views.Post_new,name='post_new'),
  path('<int:pk>/', views.post_detail, name='post_detail'),
  path('post_list/',views.post_list,name='post_list'),
  # path('home/',views.home,name='home')
]