from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from instagram.forms import PostForm
from instagram.models import Post

# Create your views here.
# CBV (post_list)
# @login_required(Post) # 장식자 예 2
post_list = ListView.as_view(model=Post,template_name='post_list.html',queryset=Post.objects.all()) # 쿼리셋 옵션에 쿼리셋을 등록하면 모델명(소문자)_list로 변수가 전달됨
# FBV (post_list)
# @login_required # 장식자 예 1
# def post_list(request):
#   qs = Post.objects.all(pk=User.pk)
#   q = request.GET.get('q','')
#   if q:
#     qs = qs.filter(title__icontains=q) # 모델의 title 속성 중 q 인자에 삽입된 값이 포함된 값을 __icontains 인자로서 검색을 구현한다.
#   return render(request,'post_list.html',{'qs' : qs,'q' : q})

def Post_form(request):
  if request.method == 'post':
    form = PostForm(request.POST,request.FILES) # 폼에서 데이터를 날리면 해당 구문으로 데이터를 받는다. (속성 대문자 주의)
    if form.is_valid():
      post = form.save() # commit=True가 default. 객체를 생성하고 save()를 해야 실제 DB에 값이 저장이 된다.
      return redirect(post) # 모델에 get_absolute_url이 구현되어 있으면 이동.
  else:
    form = PostForm() # 파일 로딩이 안됐으므로, 유효성 검사에 적합한 값을 넣도록 다시 되돌린다.
    return render(request,'post_form.html',{'form' : form})

# FBV (detail)
# def post_detail(request, id):
#   post = get_object_or_404(Post, id=id) # 옵션은 모델과 id에 id 파라미터 지정. get_object_or_404 : 객체가 존재하지 않을 때 get()을 사용하여 Http404 예외를 발생.
#   return render(request, 'post_detail.html',{'post' : post,})
# CBV
post_detail = DetailView.as_view(model=Post,pk_url_kwarg='pk',template_name='post_detail.html')
