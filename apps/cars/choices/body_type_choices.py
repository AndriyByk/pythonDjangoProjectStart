from django.db import models


class BodyTypeChoices(models.TextChoices):
    Sedan: 'Sedan'
    Hatchback: 'Hatchback'
    Coupe: 'Coupe'
    Convertible: 'Convertible'
    Station_Wagon : 'Station_Wagon'
    Minivan: 'Minivan'
    Crossover: 'Crossover'
    Sports_Car: 'Sports_Car'
