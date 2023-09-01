"""
URL configuration for gabster_act project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #para mainclude ung views ng posts app
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view, register_view, logout_view, profile_view
from .views import *
from templates import *
from general.views import home_screen_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
   # path('', include('accounts.urls')),
    path('Post/', include('Post.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    #path('accounts/', include('accounts.urls')),
    #path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)