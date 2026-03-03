from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Ryman Project',
        'subjudul' : 'Selamat datang',
        'banner' : 'Ryman Project',
    }
    return render(request, 'index.html', context)
