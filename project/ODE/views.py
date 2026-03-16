from django.shortcuts import render

from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'judul' : 'PDB - Ryman Project',
        'Posts' : posts,
        'category' : 'Persamaan Diferensial Biasa'
    }
    return render(request, 'ODE/index.html', context)


def categoryPost(request, categoryInput):
    pass


def detailPost(request, slugInput):
    pass