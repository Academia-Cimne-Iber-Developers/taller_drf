from django.contrib import admin
from .models import Autor


# Register your models here.
@admin.register(Autor)
class AutorModel(admin.ModelAdmin):
    list_display = [
        "nombre",
        "creado_en",
        "actualizado_en",
    ]
    search_fields = ["nombre"]
    ordering = ["nombre"]
    readonly_fields = ["creado_en", "actualizado_en"]
    fieldsets = (
        (
            "Información del autor",
            {
                "fields": (
                    "nombre",
                    "bio",
                )
            },
        ),
        (
            "Metadatos",
            {
                "fields": ("creado_en", "actualizado_en"),
                "classes": ("collapse",),
            },
        ),
    )
