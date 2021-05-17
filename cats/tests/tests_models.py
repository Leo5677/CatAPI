from django.test import TestCase
from model_mommy import mommy
from random import choice, randint
from cats.models import Cat

"""
Feito para testar a criação e alguns recursos do model "Cat".

Instruções:
1. Realizar o migrate, criar um superuser, acessar o admin.
2. Executar o seguinte comando no terminal: coverage run manage.py test

Para melhor visualização do resultado dos testes:
1. Executar o seguinte comando no terminal: cd htmlcov
2. Em seguida: py -m http.server
3. Acessar http://127.0.0.1:8000 em seu navegador.
"""

list_breed = ["Amgorá", "Maine Coon", "Siamês", "Bengala", "Ragdoll", "Persa"]
list_location = ["AC", "AL", "AP", "AM", "BA", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB",
                 "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
list_body = ["Cobby", "Médio", "Estrangeiro", "Semi-Estrangeiro"]


class CatTest(TestCase):
    """
    Classe para os testes de criação de objetos do model Cat e para alguns campos.
    """

    def setUp(self):
        """ Deve criar através do recurso model_mommy (um auxiliar para testes), um objeto de nossa tabela """
        self.cat = mommy.make('Cat')

    def test_cria_gato(self):
        """ Deve criar 20 objetos de nossa tabela mas sem o recurso model_mommy. """
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
        """ Deve verificar se a string do nosso objeto Cato, corresponde com a raça. """
        self.assertEquals(str(self.cat), self.cat.breed)

    def test_cria_novo_location_origin(self):
        """ Deve verificar se o location_origin está de acordo com a lista pré disposta para seleção em nosso model."""
        if self.cat.location_origin not in list_location:
            raise ValueError('Não é possível criar um novo local de origem de um gato.')
        else:
            return

    def test_cria_coat_length_negativo(self):
        """ Não deve criar um coat_legth com valor negativo, retornando um ValueError ao usuário """
        if self.cat.coat_length == randint(-21, 0) / 100:
            raise ValueError('Não é possível preencher com valores negativos')
        else:
            return

    def test_cria_novo_body_type(self):
        """ Deve verificar se o body_type está de acordo com a lista pré disposta para seleção em nosso model."""
        if self.cat.body_type not in list_body:
            raise ValueError('Não é possível criar um novo "body type" de um gato.')
        else:
            return
