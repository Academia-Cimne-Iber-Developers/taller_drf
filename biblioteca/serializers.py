from rest_framework import serializers
from .models import Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

    def validate(self, autor):
        if autor.get("bio", "") == "":
            raise serializers.ValidationError("La bio no puede estar vacía")
        elif autor.get("nombre", "") == "":
            raise serializers.ValidationError("La nombre no puede estar vacía")
        return autor
