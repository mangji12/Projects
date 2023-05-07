from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView

from instagram.forms import PostForm
from instagram.models import Post

# Create your views here.
post = ListView.as_view(model=Post,template_name='post_list.html',queryset=Post.objects.all()) # 쿼리셋 옵션에 쿼리셋을 등록하면 모델명(소문자)_list로 변수가 전달됨
def Post_new(request):
  if request.method == 'Post':
    form = PostForm(request.Post,request.Files)
    if form.is_valid():
      post = form.save()
      return redirect(post)
  else:
    form = PostForm() # 파일 로딩이 안됐으므로, 유효성 검사에 적합한 값을 넣도록 다시 되돌린다.
    return render(request,'post_new.html',{'form' : form})