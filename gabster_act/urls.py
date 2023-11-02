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
from django.template.defaulttags import url
from django.urls import path, include, re_path  # para mainclude ung views ng posts app
from django.conf import settings
from django.conf.urls.static import static
from testimonials import views
from testimonials.views import view_testimonials, testimonial_detail, add_testimonial, delete_testimonial
from accounts.views import login_view, register_view, logout_view, customization
from .views import *
from templates import *
from testimonials import views
from general.views import home_screen_view
# from django.conf.urls import url
# from accounts.views import *
from accounts import views
from django.contrib.auth import views as auth_views
from Post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('', include('accounts.urls')),
    path('', include('contact.urls')),

    # path('post/', post, name='post'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', profile_view, name='profile'),
    re_path(r'^testimonials/(?P<user_to_username>[\w.@+-]+)/$', view_testimonials, name='view_testimonials'),
    re_path(r'^testimonials/(?P<user_to_username>[\w.@+-]+)/(?P<testimonial_id>\d+)/$', testimonial_detail,
            name='testimonial_detail'),
    re_path(r'^addtestimonials/(?P<user_to_username>[\w.@+-]+)/$', add_testimonial, name='add_testimonial'),
    re_path(r'^testimonials/(?P<user_to_username>[\w.@+-]+)/delete/(?P<testimonial_id>\d+)/$', delete_testimonial,
            name='delete_testimonial'),

    re_path(r'^createpost/(?P<username>[\w.@+-]+)/$', create_post, name='create_post'),
    re_path(r'^customization/(?P<username>[\w.@+-]+)/$', customization, name='customization'),
    # re_path(r'^post/(?P<post_id>\d+)/$', post_detail, name='post_detail'),
    re_path(r'^profile/(?P<username>[\w.@+-]+)/(?P<post_id>\d+)/$', post_detail, name='post_detail'),
    path('', include('Post.urls')),

    path('verification/', include('verify_email.urls')),
    path('email_verification_sent/', views.resend_email_ver, name='email_verification_sent'),
    path('email_verification_success/', views.email_ver_success, name='email_verification_success'),

    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),

    path('search/', search, name='search'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name='reset_password'),
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
