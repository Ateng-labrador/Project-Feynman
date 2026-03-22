from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'PDP - Ryman Project',
        'Categories' : categories,
        'Posts' : posts
    }
    return render(request, 'PDE/index.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category = categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'ODE - Ryman Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'PDE/category.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'PDE - Rymann Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'PDE/detail.html', context)
