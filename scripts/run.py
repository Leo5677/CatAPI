from random import randint, choice
from cats.models import Cat


def run():
    list_breed = ["Amgorá", "Maine Coon", "Siamês", "Bengala", "Ragdoll", "Persa"]
    list_location = ["AC", "AL", "AP", "AM", "BA", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB",
                     "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    list_body = ["Cobby", "Médio", "Estrangeiro", "Semi-Estrangeiro"]

    for i in range(3):
        Cat.objects.create(
            breed=choice(list_breed),
            location_origin=choice(list_location),
            coat_length=randint(0, 21)/10,
            body_type=choice(list_body),
            pattern=f"Gato {i + 1}",
        )
