from rest_framework.viewsets import ModelViewSet
from .models import Autor
from .serializers import AutorSerializer
from rest_framework import permissions


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    # Permisos Estáticos

    # Para admitir solo usuarios autenticados
    # permission_classes = [permissions.IsAuthenticated]

    # Para admitir solo usuarios autenticados y superusuarios
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    # Para admitir a cualquier usuario, incluidos los no autenticados (comportamiento predeterminado)
    # permission_classes = [permissions.AllowAny]

    # Permisos Dinámicos
    # def get_permissions(self):
    #     """Permisos personalizados:
    #     - Operaciones de escritura requieren autenticación (create, update, partial_update, destroy).
    #     - Operaciones de lectura no requieren autenticación (list, retrieve).
    #     """
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]
