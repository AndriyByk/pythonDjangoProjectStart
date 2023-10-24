from django.core import validators
from django.db import models

from core.enums.regex_enum import RegEx
from core.models import BaseModel
from apps.users.models import UserModel


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=25, validators=[validators.RegexValidator(RegEx.AUTO_PARK_NAME.pattern,
                                                                                 RegEx.AUTO_PARK_NAME.msg)])
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='auto_parks')
