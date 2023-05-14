from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
from accounts.models import User

'''
회원가입 폼을 보통 이렇게 만들지는 않는다.
class SignupForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','password']
'''
# 정석(?)적인 방법
class SignupForm(UserCreationForm):

  # 필수 삽입 칸 커스텀. False -> True로 바꿈
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['email'].required = True
    self.fields['first_name'].required = True
    self.fields['last_name'].required = True

  # 입력을 받을 칸 커스텀. UserCreationForm의 메타 속성을 상속 받아서 overwrite.
  class Meta(UserCreationForm.Meta):
    model = User
    fields = ['username','email','first_name','last_name',]
  # pass

  # 이메일 중복 유효성 검사
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if email:
      qs = User.objects.filter(email=email) # 해당 코드가 존재하는지 검사.
      if qs.exists():
        # raise : 에러 발생 문법
        raise forms.ValidationError('이미 등록된 이메일 주소입니다.')
    return email

class ProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['profile','first_name','last_name','website_url','bio','gender']

class PasswordChangeForm(AuthPasswordChangeForm):
  # 패스워드가 기존의 것과 같은지 검사, password2는 아랫 칸에 해당 로직이 구현된다.
  def clean_new_password2(self):
    old_password = self.cleaned_data.get('old_password')
    new_password1 = super().clean_new_password2()
    # 커스텀(자체 코드 없음)
    if old_password and new_password1:
      if old_password == new_password1:
        raise forms.ValidationError('새로운 비밀번호를 입력하세요')
      return new_password1
