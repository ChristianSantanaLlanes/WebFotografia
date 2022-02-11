from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=50, help_text='Con un limite de 50 caracteres')
    contenido=models.TextField(max_length=3000, help_text='Con un limite de 3000 caracteres')
    imagen=models.ImageField(upload_to='static/subidas/blog', null=True, blank=True, help_text='Mande una foto pequena')
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    usuario=models.CharField(max_length=50)
    correo=models.EmailField()
    web=models.CharField(max_length=50, blank=True, null=True)
    comentario=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.correo