from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

'''
보통 이렇게 만들지는 않는다.
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

  # 입력 칸 커스텀. UserCreationForm의 메타 속성을 상속 받아서 overwrite.
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