from django import forms
from .models import Publicacion, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'imagen']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }
