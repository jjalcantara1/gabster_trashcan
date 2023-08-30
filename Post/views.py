from django.shortcuts import render
from .models import *
from django.views.generic import ListView


# Create your views here.
class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/list_view.html'



