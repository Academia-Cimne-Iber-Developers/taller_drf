from django.http import HttpResponse
import datetime


def welcome(request):
    now = datetime.datetime.now()
    return HttpResponse(
        f"Bienvenido a la biblioteca 'Mar de tinta'. La hora del servidor es {now.strftime('%A, %d %B, %Y a las %X')}."
    )
