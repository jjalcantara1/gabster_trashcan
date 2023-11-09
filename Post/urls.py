from django.contrib import admin
from django.urls import path, include, re_path  # para mainclude ung views ng tweets app
from django.conf import settings
from django.conf.urls.static import static

from comment.views import comment_post
from .import views
from .views import *
from templates import *


urlpatterns = [
    path('profile/<str:username>/<int:post_id>/like/', like, name='like'),
    path('get-likes/<str:username>/<int:post_id>/', views.get_likes, name='get_likes'),
    path('profile/<str:username>/<int:post_id>/likedby', likedby, name='likedby'),
    path('profile/<str:username>/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('comment_post/<int:post_id>/', comment_post, name='comment_post'),

]
