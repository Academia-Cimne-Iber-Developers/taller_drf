from django.db import models


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"
