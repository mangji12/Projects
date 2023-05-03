from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView

from instagram.models import Post

# Create your views here.
# CBV
# post_list = ListView.as_view(model=Post) # post_list 변수는 쿼리셋이다.
# FBV
def post_list(request, pk):
  post = get_object_or_404(Post, pk=pk) # 오류가 나면 404 처리를 한다.
  # try:
  #   qs = Post.objects.get(pk=pk) # pk 파라미터에 지정된 pk 값 저장.
  # except Post.DoesNotExist:
  #   raise Http404
  return render(request, 'post_list.html')