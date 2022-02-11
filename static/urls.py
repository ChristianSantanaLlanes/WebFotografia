from django.urls import path
from Galerya import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('galerya/', views.galerya),
    path('contact/', views.contacto),
    path('portafolio/<id>', views.portafolio),
    path('portafolio/portafoliosingle/<id>', views.portafolio_single),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)