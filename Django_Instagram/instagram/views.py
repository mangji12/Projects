from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from instagram.models import Tag, Post
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

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'post_detail.html',{
    'post':post
  })

def user_page(request, username):
  page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
  post_list = Post.objects.filter(author=page_user)
  post_list_count = post_list.count()
  return render(request, 'user_page.html',{'page_user':page_user,'post_list':post_list,'post_list_count':post_list_count})

