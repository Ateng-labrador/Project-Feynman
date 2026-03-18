from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Ryman Project',
    }
    return render(request, 'index.html', context)
