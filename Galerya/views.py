from random import random
from django.shortcuts import render, HttpResponse
import datetime
from .models import Fotos, Secciones, Album

def tiempo():
    t = datetime.datetime.now()
    print(t)
    ahora=0
    ahora = t.year
    anno_create = 2022
    
    if ahora == anno_create:
        return f"{ahora}"
    else:
        return f"{anno_create} - {ahora}"

texto = tiempo()
link = 't.me/ChrisVis'        

# Create your views here.
def index(request):
    categorias=Secciones.objects.all()
    return render(request, 'index.html', {"texto":texto, "link":link, "categorias":categorias})

def about(request):
    
    return render(request, 'about.html')

def galerya(request):
    
    fotos = Fotos.objects.all()
    return render(request, 'gallery.html', {"texto":texto, "link":link, "fotos":fotos})

def contacto(request):
    
    return render(request, 'contact.html')

def portafolio(request, id):
    
    seccion=Secciones.objects.filter(id=id)[0]
    albumes=Album.objects.filter(seccion=seccion)
    
    return render(request, 'portfolio.html', {"seccion":seccion, "albumes":albumes})

def portafolio_single(request, id):
    
    album=Album.objects.get(id=id)
    fotos=Fotos.objects.filter(album=album)
    return render(request, 'portfolio_single.html', {"fotos":fotos, "album":album})