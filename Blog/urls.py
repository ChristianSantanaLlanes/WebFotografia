from django.urls import path
from . import views

urlpatterns = [
    path('', views.post),
    path('blogsingle/<id>', views.post_single)
]