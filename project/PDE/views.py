from django.shortcuts import render

from .models import Post, PostIntroduction

# Create your views here.
def index(request):
    posts = Post.objects.all()
    posts_front = PostIntroduction.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'PDP - Feynman Project',
        'Categories' : categories,
        'Postsf' : posts_front,
        'Posts' : posts,
    }
    return render(request, 'PDE/index.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category = categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'ODE - Feynman Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'PDE/category.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'PDE - Feynman Project',
        'Categories' : categories,
        'Posts' : posts,
    }
    return render(request, 'PDE/detail.html', context)
