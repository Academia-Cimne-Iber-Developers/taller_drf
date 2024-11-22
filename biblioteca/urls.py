from django.urls import path
from .views import welcome, get_autors, get_autors_as_json


urlpatterns = [
    path("welcome", welcome),
    path("autores", get_autors),
    path("autores/json", get_autors_as_json),
]
