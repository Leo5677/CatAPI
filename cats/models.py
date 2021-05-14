from django.db import models
from CatAPI.utils import *


# Create your models here.


class Cat(models.Model):
    breed = models.CharField('Raça', max_length=100, choices=RACA_CHOICES)
    location_origin = models.CharField('Local de Origem', max_length=100, choices=LOCAL_CHOICES)
    coat_length = models.PositiveSmallIntegerField('Comprimento da Pelagem')
    body_type = models.CharField('Tipo de Corpo', max_length=100, choices=TIPOS_CHOICES)
    pattern = models.CharField('Padrão', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'
        ordering = ['id']

    def __str__(self):
        return f'{self.breed} | {self.body_type} | {self.location_origin}'

