from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Judul' : 'Fynman Project',
        'subjudul' : 'Selamat Datang',
        'banner' : '',
        'app_css' : 'about/css/style.css'
    }
    return render(request, 'about/index.html', context)
