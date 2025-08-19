
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm


# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Publicacion, ContadorVisitas
from .forms import PublicacionForm, ComentarioForm


def home(request):
    # Obtenemos o creamos la publicación por defecto
    publicacion, _ = Publicacion.objects.get_or_create(
        id=1,
        defaults={
            "titulo": "Promo del mes",
            "contenido": "Actualizá esta publicación desde el botón Editar.",
            "imagen": None
        }
    )

    # Contador de visitas
    contador, _ = ContadorVisitas.objects.get_or_create(id=1)
    contador.cantidad += 1
    contador.save()

    # Solo mostramos comentarios aprobados
    comentarios = publicacion.comentarios.filter(aprobado=True).order_by("-fecha_creacion")

    # Procesar envío de comentario
    if request.method == "POST":
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.save()
            return redirect("home")  # recargar para evitar reenvío
    else:
        comentario_form = ComentarioForm()

    return render(request, "home.html", {
        "publicacion": publicacion,
        "comentarios": comentarios,
        "comentario_form": comentario_form,
        "contador": contador if request.user.is_superuser else None,  # solo admins lo ven
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def editar_publicacion(request):
    publicacion, _ = Publicacion.objects.get_or_create(
        id=1,
        defaults={
            "titulo": "Promo del mes",
            "contenido": "Actualizá esta publicación desde este formulario.",
            "imagen": None
        }
    )

    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, "editar_publicacion.html", {"form": form})
