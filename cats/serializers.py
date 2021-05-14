from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = (
            'id',
            'breed',
            'location_origin',
            'coat_length',
            'body_type',
            'pattern',
        )
