from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kalkulus - Ryman Project'
    }
    return render(request, 'base.html', context)