from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Kalkulus - Ryman Project',
        'Categories' : categories,
        'Posts': posts,
    }
    return render(request, 'kalkulus/index.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category = categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Kalkulus - Ryman Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'kalkulus/category.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Kalkulus - Rymann Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'kalkulus/detail.html', context)
