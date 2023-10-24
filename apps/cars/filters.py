from django_filters import rest_framework

from .choices.body_type_choices import BodyTypeChoices
from .models import CarModel


class CarFilter(rest_framework.FilterSet):
    year_lt = rest_framework.NumberFilter('year', 'lt')
    year_lte = rest_framework.NumberFilter('year', 'lte')
    year_gt = rest_framework.NumberFilter('year', 'gt')
    year_gte = rest_framework.NumberFilter('year', 'gte')
    year = rest_framework.RangeFilter('year')

    brand_starts = rest_framework.CharFilter('brand', 'startswith')
    brand_ends = rest_framework.CharFilter('brand', 'endswith')
    brand_contains = rest_framework.CharFilter('brand', 'contains')


    seats_lt = rest_framework.NumberFilter('seats', 'lt')
    seats_lte = rest_framework.NumberFilter('seats', 'lte')
    seats_gt = rest_framework.NumberFilter('seats', 'gt')
    seats_gte = rest_framework.NumberFilter('seats', 'gte')

    volume_lt = rest_framework.NumberFilter('volume', 'lt')
    volume_lte = rest_framework.NumberFilter('volume', 'lte')
    volume_gt = rest_framework.NumberFilter('volume', 'gt')
    volume_gte = rest_framework.NumberFilter('volume', 'gte')

    # cab_type_starts = rest_framework.CharFilter('cab_type', 'startswith')
    # cab_type_ends = rest_framework.CharFilter('cab_type', 'endswith')
    # cab_type_contains = rest_framework.CharFilter('cab_type', 'contains')
    cab_type = rest_framework.ChoiceFilter('cab_type', choices=BodyTypeChoices.choices)

    order = rest_framework.OrderingFilter(
        fields=(
            'id',
            'brand',
            'year',
            'cab_type',

            '-id',
            '-brand',
            '-year',
            '-cab_type',

            # ('price', 'asd')
        )
    )
