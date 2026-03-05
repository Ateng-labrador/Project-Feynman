from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kalkulus - Ryman Project'
    }
    return render(request, 'kalkulus/index.html', context)