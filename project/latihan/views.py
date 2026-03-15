from django.shortcuts import render

# slug ada pita link untuk menuju konten


# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' :'Latihan- Ryman Project',
        'Categories' : categories,
        'Posts' : posts
    }
    return render(request,  'latihan/index.html', context)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Ryman Project',
        'Categories' : categories,
        'posts' : posts,
    }
    return render(request, 'latihan/category.html', context)

def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'judul' : 'Ryman Project',
        'categories' : categories,
        'posts' : posts,
    }
    return render(request, 'latihan/detail.html', context)
