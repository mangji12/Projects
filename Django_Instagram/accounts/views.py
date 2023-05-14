from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth import login as login_auth
from accounts.forms import SignupForm
from django.contrib import messages

# Create your views here.
# profile view
profile_edit = UpdateView.as_view(template_name='profile_edit_form.html')

# login
login = LoginView.as_view(template_name='login_form.html')
# def login(request):
#   pass

# logout
logout = LogoutView.as_view()
# 로그아웃 하자마자 로그인 페이지로 이동 설정
# def logout(logout_then_login):
#   messages.success(request, '로그아웃되었습니다.')
#   return logout_then_login(request)

def signup(request):
  if request.method == 'POST':
    # 폼 인자로 템플릿에서 사용할 폼 형식을 보낸다.
    form = SignupForm(request.POST)
    # 전달된 데이터가 유효한지 검사 : is_valid
    if form.is_valid():
      signed_user = form.save()
      login_auth(request, signed_user)

      # 사용자 객체가 user 변수에 전달. -> 인스턴스로서 사용가능. ex) 모델(User)의 user.website_url, user.bio 등등
      # user = form.save()

      # 모델에 get_absolute_url()을 지정했다면 이렇게만 입력해도 리다이렉트 가능.
      # return redirect(user)

      messages.success(request,'회원가입 환영합니다.')

      # 회원가입시 생기는 next인자를 어떻게 처리할 것인지 설정
      next_url = request.GET.get('next','/')
      return redirect(next_url)
  else:
    form = SignupForm()
  return render(request,'signup_form.html',{'form':form})