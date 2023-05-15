from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from instagram.models import Tag
from django.contrib import messages
from instagram.forms import PostForm


# Create your views here.

@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      # 모델에 작성할 수도 있음
      # for tag_name in post.extract_tag_list():
      #   tag, _ = Tag.objects.get_or_create(name='tag_name')
      post.tag_set.add(*post.extract_tag_list())
      messages.info(request, '포스팅을 저장했습니다.')
      return redirect('/')
  else:
    # get 요청일때
    form = PostForm()
  return render(request, 'post_form.html',{
    'form':form
  })