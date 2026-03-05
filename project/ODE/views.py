from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'PDB - Ryman Project'
    }
    return render(request, 'ODE/index.html', context)
