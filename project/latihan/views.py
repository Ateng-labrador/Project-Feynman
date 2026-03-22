from django.shortcuts import render
from .models import Quiz,Post
from django.views.generic import ListView
from django.http import JsonResponse

# slug ada pita link untuk menuju konten

# Create your views here. 

def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' :'Latihan - Ryman Project',
        'Categories' : categories,
        'Posts' : posts
    }
    return render(request,  'latihan/index.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Latihan - Ryman Project',
        'Categories' : categories,
        'posts' : posts,
    }
    return render(request, 'latihan/category.html', context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Latihan - Ryman Project',
        'categories' : categories,
        'posts' : posts,
    }
    return render(request, 'latihan/detail.html', context)
