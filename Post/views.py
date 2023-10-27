from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.models import UserAccount
from .models import Post, UserLike
from django.urls import reverse_lazy
from django import forms
from Post.forms import PostForm
from django.contrib import messages


@login_required
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


@login_required
def post_detail(request, post_id,username):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    liked_users = post.liked_by.all()
    user_like = UserLike.objects.get(voter=user, post=post)
    return render(request, 'posts/posts_detail.html', {'post': post,
                                                       'liked_users': liked_users,
                                                       'user_like': user_like})


@login_required
def like(request, username, post_id):
    user = request.user
    target_post = Post.objects.get(pk=post_id)

    try:
        user_like, created = UserLike.objects.get_or_create(voter=user, post=target_post)

        if created:
            target_post.likes += 1
            target_post.save()
            target_post.likes.add(user)
        elif not user_like.is_liked:
            user_like.is_liked = True
            user_like.save()
            target_post.likes += 1
            target_post.save()
            target_post.liked_by.add(user)
        else:
            user_like.is_liked = False
            user_like.save()
            target_post.likes -= 1
            target_post.save()
            target_post.liked_by.remove(user)

        return JsonResponse({'likes': target_post.likes})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'The post does not exist.'}, status=404)


@login_required
def get_likes(request, post_id, username):
    post = get_object_or_404(Post, pk=post_id)
    liked_users = [user.username for user in post.liked_by.all()]
    return JsonResponse({'liked_users': liked_users})


@login_required
def likedby(request, post_id, username):
    post = Post.objects.get(id=post_id)
    liked_users = UserLike.objects.filter(post=post, is_liked=True)
    return render(request, 'posts/liked_by.html', {'post': post, 'liked_users': liked_users})


@login_required
def customization(request, username):
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

    return render(request, 'customization/customization.html', {'form': form})
