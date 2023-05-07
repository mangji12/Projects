from django import forms

from instagram.models import Post


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    # 전체 필드 지정. 혹은 list로 읽어올 필드명 지정
    fields = '__all__'