from django.contrib import admin
from .models import Publicacion, Comentario

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_actualizacion")


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "publicacion", "aprobado", "fecha_creacion")
    list_filter = ("aprobado", "fecha_creacion")
    search_fields = ("nombre", "contenido")
    actions = ["aprobar_comentarios"]

    def aprobar_comentarios(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_comentarios.short_description = "Aprobar comentarios seleccionados"
