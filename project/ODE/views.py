from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'ODE - Ryman Project',
        'Categories' : categories,
        'Posts' : posts
    }
    return render(request, 'ODE/index.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    context ={
        'judul' : 'ODE - Ryman Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'ODE/category.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'ODE - Ryman Project',
        'Categories' : categories,
        'posts' : posts,
    }
    return render(request, 'ODE/detail.html', context)
