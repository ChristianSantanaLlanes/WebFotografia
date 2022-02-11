from django.db import models

# Create your models here.

class Secciones(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=5000, blank=True, null=True)
    imagen=models.ImageField(upload_to='static/subidas/secciones', null=True, help_text='Las fotos deben ser 675x675 ')
    
    def __str__(self):
        return self.nombre
    
class Album(models.Model):
    seccion=models.ForeignKey(Secciones, on_delete=models.CASCADE, null=True)
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField(max_length=1000)
    imagen=models.ImageField(upload_to='static/subidas/album', help_text='La foto de tu album')
    
    def __str__(self):
        return self.nombre
    
class Fotos(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    nombre=models.CharField(max_length=50, help_text="Inserte un nombre para la foto")
    foto=models.ImageField(null=True, upload_to='static/subidas/fotos')
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre