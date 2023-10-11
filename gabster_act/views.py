from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserAccount

# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/home.html', context)

def profile_view(request, username):
    # print(request.user.username)
    user = get_object_or_404(UserAccount, username=username)
    # user = get_object_or_404(UserAccount, username=username)
    # print(user)
    # Add any additional data or context you want to pass to the user profile template
    context = {
        'user': user,
        'person': request.user,
        'asd': 'asd',
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
