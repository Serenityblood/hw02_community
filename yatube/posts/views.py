from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Group, Post, User


def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_list = group.posts.all()
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    author_username = get_object_or_404(User, username=username)
    author_posts = Post.objects.filter(author=author_username)
    paginator = Paginator(author_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'name': author_username
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    text = post.text[:30]
    context = {
        'post': post,
        'text': text,
        'post_count': post_count
    }
    return render(request, 'posts/post_detail.html', context)
