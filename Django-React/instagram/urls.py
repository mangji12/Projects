from django.urls import path

from instagram import views
app_name = 'instagram'
urlpatterns = [
  path('new/', views.post_new, name='post_new'),
  path('<int:pk>/', views.post_detail, name='post_detail'),
  path('<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('',views.post_list, name='post_list'),
  # path('home/',views.home,name='home')
]