from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'PDP - Ryman Project'
    }
    return render(request, 'PDE/index.html', context)
