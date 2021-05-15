from django.test import TestCase
from model_mommy import mommy
from random import choice, randint
from cats.models import Cat

# Create your tests here.


list_breed = ["Amgorá", "Maine Coon", "Siamês", "Bengala", "Ragdoll", "Persa"]
list_location = ["AC", "AL", "AP", "AM", "BA", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB",
                 "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
list_body = ["Cobby", "Médio", "Estrangeiro", "Semi-Estrangeiro"]


class CatTest(TestCase):
    def setUp(self):
        self.cat = mommy.make('Cat')

    def test_cria_gato(self):
        for i in range(20):
            Cat.objects.create(
                breed=choice(list_breed),
                location_origin=choice(list_location),
                coat_length=randint(0, 21) / 10,
                body_type=choice(list_body),
                pattern=f"Gato {i + 1}",
            )
        return

    def test_str_gato(self):
        self.assertEquals(str(self.cat), self.cat.breed)

    def test_cria_location(self):
        if self.cat.location_origin not in list_location:
            raise ValueError('Não é possível criar um novo local de origem de um gato.')
        else:
            return

    def test_cria_valor_negativo(self):
        if self.cat.coat_length == randint(-21, 0) / 100:
            raise ValueError('Não é possível preencher com valores negativos')
        else:
            return

    def test_cria_body(self):
        if self.cat.body_type not in list_body:
            raise ValueError('Não é possível criar um novo "body type" de um gato.')
        else:
            return
