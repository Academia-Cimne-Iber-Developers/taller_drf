from django.http import HttpResponse, JsonResponse
import datetime
from .models import Autor


def welcome(request):
    now = datetime.datetime.now()
    return HttpResponse(
        f"Bienvenido a la biblioteca 'Mar de tinta'. La hora del servidor es {now.strftime('%A, %d %B, %Y a las %X')}."
    )


def get_autors(request):
    """
    Devolver todos los autores con un formato HTML
    """
    # Obtener todos los autores
    autores = Autor.objects.all()

    # Crear una respuesta con los autores
    response = "<h1>Autores</h1>"
    for autor in autores:
        response += f"<h3>{autor.nombre}</h3>"
        response += f"<p>{autor.bio}</p>"
        response += f"<p>Creado en: {autor.creado_en} - Actualizado en: {autor.actualizado_en}</p>"

    return HttpResponse(response)


def get_autors_as_json(request):
    """
    Devolver todos los autores con un formato JSON
    """
    # Obtener todos los autores
    autores = Autor.objects.all()

    # Crear un diccionario con los autores para serializarlo a JSON
    response = {"autores": []}
    for autor in autores:
        response["autores"].append(
            {
                "nombre": autor.nombre,
                "bio": autor.bio,
                "creado_en": autor.creado_en,
                "actualizado_en": autor.actualizado_en,
            }
        )

    return JsonResponse(response)
