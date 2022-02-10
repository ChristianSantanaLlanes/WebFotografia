from django.contrib import admin
from .models import Categoria, Comentario, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('titulo', 'imagen', 'autor', 'categoria')
    search_fields=('autor', 'titulo')
    list_filter=('autor', 'categoria')
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display=('usuario', 'correo', 'comentario', 'web')
    list_filter=('correo', 'web', 'usuario')
    search_fields=('usuario', 'correo', 'web')

admin.site.register(Categoria)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)