from django.shortcuts import render, redirect

from Post.models import Post
from accounts.models import UserAccount


def admin_panel(request):
    return render(request, 'admin/admin_panel.html')


def admin_user(request):
    if request.method == 'POST':
        if 'select_delete' in request.POST:
            user_ids_to_delete = request.POST.getlist('delete_user')
            UserAccount.objects.filter(id__in=user_ids_to_delete).delete()

            return redirect('admin_panel_users')  # Refreshes the page

    users = UserAccount.objects.all()  # Displays all users

    return render(request, 'admin/admin_user.html', {'users': users})


def admin_post(request):
    if request.method == 'POST':
        if 'select_delete' in request.POST:
            post_ids_to_delete = request.POST.getlist('delete_post')
            Post.objects.filter(id__in=post_ids_to_delete).delete()

            return redirect('admin_panel_posts')  # Refreshes the page

    posts = Post.objects.all()  # Displays all posts

    return render(request, 'admin/admin_post.html', {'posts': posts})
