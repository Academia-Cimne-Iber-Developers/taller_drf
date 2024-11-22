from django.urls import path, include
from .views import welcome, get_autors, get_autors_as_json
from rest_framework.routers import DefaultRouter
from .viewsets import AutorViewSet

router = DefaultRouter()

router.register(r"autors", AutorViewSet)

urlpatterns = [
    path("welcome", welcome),
    path("autores", get_autors),
    path("autores/json", get_autors_as_json),
    path("", include(router.urls)),
]
