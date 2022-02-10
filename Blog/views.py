from django.shortcuts import render, HttpResponse
from .models import Post, Comentario

# Create your views here.

def post(request):
    
    posts=Post.objects.all()
    return render(request, 'blog.html', {"posts":posts})

def post_single(request, id):
    
    post=Post.objects.filter(id=id)[0]
    
    if request.method=='POST':
        nombre=request.POST["nombre"]
        correo=request.POST['email']
        web=request.POST['web']
        comentario=request.POST['comentario']
        Comentario.objects.create(post=Post.objects.filter(id=id)[0], usuario=nombre, correo=correo, web=web, comentario=comentario)
    else:
        pass
    comentarios=Comentario.objects.filter(post=id)
    
    return render(request, 'blog_single.html', {"post":post, "comentarios":comentarios})