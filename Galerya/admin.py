from django.contrib import admin
from Galerya.models import Secciones, Fotos, Album

class SeccionesAdmin(admin.ModelAdmin):
    list_display=("nombre", "descripcion")

class FotosAdmin(admin.ModelAdmin):
    list_display=("nombre", "album", "foto", 'create', 'update')
    search_fields=("nombre",)
    list_filter=("album",)
    readonly_fields=('create', 'update')
        

# Register your models here.
admin.site.register(Secciones, SeccionesAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(Album)