from django.db import models
from CatAPI.utils import *
from django.core.validators import MinValueValidator


# Create your models here.


class Cat(models.Model):
    breed = models.CharField('Raça', max_length=100)
    location_origin = models.CharField('Local de Origem', max_length=100, choices=LOCAL_CHOICES)
    coat_length = models.DecimalField('Comprimento da Pelagem', max_digits=3, decimal_places=2,
                                      help_text="Preencha apenas com números positivos.",
                                      validators=[MinValueValidator(0.01)])
    body_type = models.CharField('Tipo de Corpo', max_length=100, choices=TIPOS_CHOICES)
    pattern = models.CharField('Padrão', max_length=100)

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'
        ordering = ['id']

    def __str__(self):
        return self.breed
