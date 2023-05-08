from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from instagram.forms import PostForm
from instagram.models import Post
from django.contrib import messages

# Create your views here.

# CBV (post_list)
post_list = ListView.as_view(model=Post,template_name='post_list.html',queryset=Post.objects.all()) # 쿼리셋 옵션에 쿼리셋을 등록하면 모델명(소문자)_list로 변수가 전달됨
# FBV (post_list)
# @login_required # 장식자 예 1
# def post_list(request):
#   qs = Post.objects.all()
#   q = request.GET.get('q','')
#   if q:
#     qs = qs.filter(title__icontains=q) # 모델의 title 속성 중 q 인자에 삽입된 값이 포함된 값을 __icontains 인자로서 검색을 구현한다.
#   messages.info(request, '새 글이 등록되었습니다.') # 상속의 부모 템플릿에 거의 적용.
#   return render(request,'post_list.html',{'qs' : qs,'q' : q})

# CBV (new)
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  form_class = PostForm
  template_name = 'post_form.html'
  def form_valid(self, form):
    self.object = form.save(commit=False) # BaseView에 있는 object 인자(옵션)에 가져온 form(PostForm)정보를 (임시)저장
    self.object.author = self.request.user # 가져온 form의 author 정보에 reuqest로 보낸 user(pk)정보를 전달.
    self.object = form.save()
    messages.info(self.request,'포스팅을 저장했습니다.') # 함수 기반 객체가 아닌 클래스 가반 뷰(CBV에서 request 객체를 반환 받을 때)
    return super().form_valid(form) # 부모의 form_valid를 호출(기본 함수 내장)

post_new = PostCreateView.as_view()
# FBV (new)
# @login_required
# def post_new(request):
#   # post = get_object_or_404(Post, pk=pk)
#   if request.method == 'POST':
#     form = PostForm(request.POST,request.FILES) # 폼에서 데이터를 날리면 해당 구문으로 데이터를 받는다. (속성 대문자 주의)
#     if form.is_valid():
#       post = form.save(commit=False) # commit=True가 default. 객체를 생성하고 save()를 해야 실제 DB에 값이 저장이 된다.
#       post.author = request.user
#       post.save()
#       # messages.add_message(request, messages,SUCCESS, '새 글이 등록되었습니다.')
#       messages.info(request, '새 글이 등록되었습니다.') # 혹은 shortcut 형태
#       return redirect(post) # 모델에 get_absolute_url이 구현되어 있으면 이동.
#   else:
#     form = PostForm() # 파일 로딩이 안됐으므로, 유효성 검사에 적합한 값을 넣도록 다시 되돌린다.
#   return render(request,'post_form.html',{'form' : form,'post':None})

# CBV
class PostDeleteView(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = reverse_lazy('post_list.html')

post_delete = PostDeleteView.as_view()
# FBV (delete)
@login_required
def post_delete(request, pk):
  post = get_object_or_404(Post,pk=pk)
  if request.method == "POST":
    post.delete()
    messages.success(request,'포스팅을 삭제하였습니다.')
    return redirect('post_list.html')
  return render(request,'post_confirm_delete.html',{'post':post})

# CBV (edit)
class PostUpdateView(LoginRequiredMixin,UpdateView):
  model = Post
  form_class = PostForm
  success_url = reverse_lazy('post_detail.html')
  template_name = 'post_form.html'

  def form_valid(self,form):
    messages.success(self.request,'포스팅을 수정하였습니다.')
    return super().form_valid(form)

post_edit = PostUpdateView.as_view()
# # FBV (edit)
# @login_required
# def post_edit(request, pk):
#   post = get_object_or_404(Post,pk=pk)
#
#   # 작성자 체크
#   if post.author != request.user:
#     messages.error(request, '작성자만 수정할 수 있습니다.')
#     return redirect(post)
#
#   if request.method == 'POST':
#     form = PostForm(request.POST,request.FILES, instance=post) # 폼에서 데이터를 날리면 해당 구문으로 데이터를 받는다. (속성 대문자 주의) ,instance 속성으로 post 쿼리셋도 가져온다.
#     if form.is_valid():
#       post = form.save(commit=False) # commit=True가 default. 객체를 생성하고 save()를 해야 실제 DB에 값이 저장이 된다.
#       post.author = request.user # 현재 로그인 User Instance
#       post = form.save()
#       messages.info(request,'포스팅을 수정하였습니다.')
#       return redirect(post) # 모델에 get_absolute_url이 구현되어 있으면 이동.
#   else:
#     form = PostForm(instance=post) # 파일 로딩이 안됐으므로, 유효성 검사에 적합한 값을 넣도록 다시 되돌린다.
#   return render(request,'post_form.html',{'form' : form,'post':post})


# CBV (detail)
post_detail = DetailView.as_view(model=Post,pk_url_kwarg='pk',template_name='post_detail.html')
# FBV (detail)
# def post_detail(request, id):
#   post = get_object_or_404(Post, id=id) # 옵션은 모델과 id에 id 파라미터 지정. get_object_or_404 : 객체가 존재하지 않을 때 get()을 사용하여 Http404 예외를 발생.
#   return render(request, 'post_detail.html',{'post' : post,})
