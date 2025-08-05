from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post


def home_page(request):
    return render(request, 'blog/home_page.html')


def post_list(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter(
    #     published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
