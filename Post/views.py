from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.models import UserAccount
from .models import Post, UserLike
from django.urls import reverse_lazy
from django import forms
from Post.forms import PostForm
from django.contrib import messages


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
    post = get_object_or_404(Post, pk=post_id)
    liked_users = post.liked_by.all()
    return render(request, 'posts/posts_detail.html', {'post': post, 'liked_users': liked_users})


@login_required
def like(request, username, post_id):
    user = request.user  # The user who is liking the post (login user)
    target_post = Post.objects.get(pk=post_id)  # The post that is being liked

    try:
        user_like, created = UserLike.objects.get_or_create(voter=user, post=target_post)
        if not created and user_like.is_liked:
            # The user has already liked the post, so remove the like
            user_like.delete()
            if target_post.likes > 0:  # Ensure likes is not negative
                target_post.likes -= 1  # Decrement the likes
                target_post.save()  # Save the changes
            # messages.success(request, f'You have removed your like for this post!')
        else:
            # The user hasn't liked the post before or had unliked it, so create a new like
            user_like.is_liked = True  # Change the like status
            user_like.save()
            target_post.likes += 1  # Increment the likes
            target_post.save()  # Save the changes
            # messages.success(request, f'You have liked this post!')

        # After liking, stay on the post's detailed view
        return redirect('post_detail', post_id=post_id)  # Redirect to the post's detailed view
    except Post.DoesNotExist:
        # Handle the case where the post does not exist
        messages.error(request, 'The post does not exist.')

    # You can add more error handling for other scenarios if needed.

