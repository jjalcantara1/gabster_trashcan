from django.shortcuts import render


# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/homepage.html', context)
