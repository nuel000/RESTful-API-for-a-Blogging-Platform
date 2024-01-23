from django.urls import path
from .views import create_get_post_view, post_detail_view, register_view, login_view

urlpatterns = [
    path('posts/', create_get_post_view, name='post-list-create'),
    path('posts/<int:pk>/', post_detail_view, name='post-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),

]