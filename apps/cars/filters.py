from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError

from .models import CarModel


def car_filtered_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in query.items():
        match k:
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'seats_gt':
                qs = qs.filter(seats__gt=v)
            case 'seats_lt':
                qs = qs.filter(seats__lt=v)
            case 'seats_gte':
                qs = qs.filter(seats__gte=v)
            case 'seats_lte':
                qs = qs.filter(seats__lte=v)

            case 'volume_gt':
                qs = qs.filter(volume__gt=v)
            case 'volume_lt':
                qs = qs.filter(volume__lt=v)
            case 'volume_gte':
                qs = qs.filter(volume__gte=v)
            case 'volume_lte':
                qs = qs.filter(volume__lte=v)

            case 'brand_sw':
                qs = qs.filter(brand__startswith=v)
            case 'brand_ew':
                qs = qs.filter(brand__endswith=v)
            case 'brand_c':
                qs = qs.filter(brand__contains=v)

            case 'cab_type_sw':
                qs = qs.filter(cab_type__startswith=v)
            case 'cab_type_ew':
                qs = qs.filter(cab_type__endswith=v)
            case 'cab_type_c':
                qs = qs.filter(cab_type__contains=v)
            # sorting
            case 'o_b_brand_asc':
                qs = qs.order_by('brand')
            case 'o_b_brand_desc':
                qs = qs.order_by('-brand')

            case 'o_b_year_asc':
                qs = qs.order_by('year')
            case 'o_b_year_desc':
                qs = qs.order_by('-year')

            case 'o_b_seats_asc':
                qs = qs.order_by('seats')
            case 'o_b_seats_desc':
                qs = qs.order_by('-seats')

            case 'o_b_cab_type_asc':
                qs = qs.order_by('cab_type')
            case 'o_b_cab_type_desc':
                qs = qs.order_by('-cab_type')

            case 'o_b_volume_asc':
                qs = qs.order_by('volume')
            case 'o_b_volume_desc':
                qs = qs.order_by('-volume')
            case _:
                raise ValidationError({'detail': f'{k} not allowed here'})

    return qs
