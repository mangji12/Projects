from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
  path('signup/',views.signup,name='signup'),
  path('login/',views.login,name='login'), # /accounts/login => settings.LOGIN_URL
  path('logout/',views.logout,name='logout'),
  path('password_change/',views.password_change,name='password_edit'),
  path('edit/', views.profile_edit, name='profile_edit'),
]