from django.shortcuts import render
from django.views.generic import CreateView, ListView

from instagram.models import Post

# Create your views here.
post_list = ListView.as_view(model=Post) # post_list 변수는 쿼리셋이다.