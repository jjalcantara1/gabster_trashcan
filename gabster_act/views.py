from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/home.html', context)

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    # Add any additional data or context you want to pass to the user profile template
    context = {
        'user': user,
    }
    return render(request, 'profile/profile.html', context)

def profile(request):
    return render(request, "profile/profile.html", {})