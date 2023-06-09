from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts import views

app_name = 'accounts'

urlpatterns = [
  path('login/',LoginView.as_view(template_name='login.html'), name='login'),
  # path('logout/', ),
  path('profile/', views.profile, name='profile'),
  path('profile/edit/',views.profile_edit, name='profile_edit'),
  path('signup',views.signup,name='signup')
]