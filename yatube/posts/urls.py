from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts_page'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
    path('posts/create', views.post_create, name='post_create'),
    path('posts/<post_id>/edit', views.post_edit, name='post_edit')
]
