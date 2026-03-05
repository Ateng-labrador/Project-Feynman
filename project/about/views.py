from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'About - Fynman Project',
        'app_css' : 'about/css/style.css'
    }
    return render(request, 'base.html', context)
