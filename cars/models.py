from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    cab_type = models.CharField(max_length=20)
    volume = models.FloatField()
