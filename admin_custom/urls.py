from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/users/', views.admin_user, name='admin_panel_users'),
    path('admin-panel/posts/', views.admin_post, name='admin_panel_posts'),
]