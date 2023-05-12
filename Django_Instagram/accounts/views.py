from django.shortcuts import render, redirect

from accounts.forms import SignupForm
from django.contrib import messages

# Create your views here.

def signup(request):
  if request.method == 'POST':
    # 폼 인자로 템플릿에서 사용할 폼 형식을 보낸다.
    form = SignupForm(request.POST,request.FILES)
    # 전달된 데이터가 유효한지 검사 : is_valid
    if form.is_valid():
      # 사용자 객체가 user 변수에 전달. -> 인스턴스로서 사용가능. ex) 모델(User)의 user.website_url, user.bio 등등
      user = form.save()
      # 모델에 get_absolute_url()을 지정했다면 이렇게만 입력해도 리다이렉트 가능.
      # return redirect(user)
      messages.success(request,'회원가입 환영합니다.')
      return redirect('/')
  else:
    form = SignupForm()
  return render(request,'signup_form.html',{'form':form})