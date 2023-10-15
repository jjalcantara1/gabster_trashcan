from django.contrib import admin
from django.urls import path, include, re_path  # para mainclude ung views ng tweets app
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from templates import *


urlpatterns = [
    # path('', PostListView.as_view(), name='list-view'),
    # path('create_post/', create_post, name='create_post'),
]
