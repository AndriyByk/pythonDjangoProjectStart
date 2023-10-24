from datetime import datetime

from django.db import models
from django.core import validators
from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from core.enums.regex_enum import RegEx
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=[validators.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    year = models.IntegerField(validators=[validators.MinValueValidator(1900), validators.MaxValueValidator(datetime.now().year)])
    seats = models.IntegerField(validators=[validators.MinValueValidator(2), validators.MaxValueValidator(12)])
    cab_type = models.CharField(max_length=20, choices=BodyTypeChoices.choices)

    volume = models.FloatField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
