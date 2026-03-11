from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    # queryset
    posts = Post.objects.all()
    context = {
        'judul' : 'Kalkulus - Ryman Project',
        'Posts': posts,
        'category' : 'Kalkulus',

    }
    return render(request, 'kalkulus/index.html', context)