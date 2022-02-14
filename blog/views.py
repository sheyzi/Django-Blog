from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)
