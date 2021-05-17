from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    """ Serializa os dados do model gato, tornando possível a integração para a API. """
    class Meta:
        model = Cat
        fields = '__all__'
