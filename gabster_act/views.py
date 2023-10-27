from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from Post.models import Post, UserLike
from accounts.models import UserAccount
from testimonials.models import Testimonial


# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/home.html', context)

def profile_view(request, username):

    user = get_object_or_404(UserAccount, username=username)
    testimonials_received = Testimonial.objects.filter(user_to=user).order_by('-createdAt')
    post = Post.objects.filter(user=user).order_by('-createdAt')
    user_like = UserLike.objects.filter(voter=user, post__in=Post.objects.all())
    print(user_like)
    context = {
        'user': user,
        'person': request.user,
        'testimonials_received': testimonials_received,
        'post': post,
        'user_like': user_like
    }
    return render(request, 'profile/profile.html', context)

def search(request):
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        users = UserAccount.objects.distinct().filter(username__icontains=search_query)

        return render(request,'profile/search.html', {'users': users})
    else:
        users = UserAccount.objects.all()

        return render(request, 'profile/search.html', {'users': users})

