from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserAccount

# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/home.html', context)

def profile_view(request, username):
    user = UserAccount(username=username)
    print(user)
    # Add any additional data or context you want to pass to the user profile template
    context = {
        'user': request.user,
    }
    return render(request, 'profile/profile.html', context)

def profile(request):
    return render(request, "profile/profile.html", {})

def post(request):
    return render(request, "posts/post.html", {})

def testimonials(request):
    return render(request, "posts/testimonials.html", {})