from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django import forms
from Post.forms import PostForm


#
# # Create your views here.
# class PostListView(ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = 'posts/list_view.html'


def create_post(request, username):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user

            post = form.save(commit=False)
            post.user = user
            post.save()

            return redirect('profile', username=username)
    else:
        form = PostForm()

    return render(request, 'posts/post.html', {'form': form})


def post_detail(request, post_id):
    # Retrieve the post based on the primary key (post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/posts_detail.html', {'post': post})