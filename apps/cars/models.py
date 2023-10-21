from django.db import models

from apps.auto_parks.models import AutoParkModel
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    cab_type = models.CharField(max_length=20)
    volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
