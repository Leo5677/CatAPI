from rest_framework import viewsets
from .models import Cat
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CatSerializer


# Create your views here.


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'location_origin', 'coat_length', 'body_type', 'pattern']


