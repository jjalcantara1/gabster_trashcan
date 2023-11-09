from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import *
from Post.models import Post


@login_required
def comment_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            username = post.user.username
            return redirect('post_detail', username=username, post_id=post_id)
    else:
        comment_form = CommentForm()

    return render(request, 'posts/posts_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': comment_form})
