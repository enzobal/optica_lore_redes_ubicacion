from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('editar-publicacion/', views.editar_publicacion, name='editar_publicacion'),
    
]