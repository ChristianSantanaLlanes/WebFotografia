from random import random
from django.shortcuts import render, redirect
import datetime
from .models import Fotos, Secciones, Album
from .forms import Contacto

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
    
    return render(request, 'about.html', {"texto":texto, "link":link})

def galerya(request):
    
    fotos = Fotos.objects.all()
    return render(request, 'gallery.html', {"texto":texto, "link":link, "fotos":fotos})

def contacto(request):
    formulario=Contacto()
    
    if request.method=='POST':
        formulario_contacto = Contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            asunto=request.POST.get('asunto')
            mensaje=request.POST.get('mensaje')
            return redirect('/contact/?valido')
    else:
        return render(request, 'contact.html', {"formulario":formulario})

def portafolio(request, id):
    
    seccion=Secciones.objects.filter(id=id)[0]
    albumes=Album.objects.filter(seccion=seccion)
    
    return render(request, 'portfolio.html', {"texto":texto, "link":link, "seccion":seccion, "albumes":albumes})

def portafolio_single(request, id):
    
    album=Album.objects.get(id=id)
    fotos=Fotos.objects.filter(album=album)
    return render(request, 'portfolio_single.html', {"texto":texto, "link":link, "fotos":fotos, "album":album})