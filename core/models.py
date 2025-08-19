from django.db import models


class Publicacion(models.Model):
    titulo = models.CharField(max_length=100, default="Título de la publicación")
    contenido = models.TextField(default="Contenido de la publicación")
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to="publicaciones/", blank=True, null=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.contenido[:20]}"

class ContadorVisitas(models.Model):
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitas: {self.cantidad}"
