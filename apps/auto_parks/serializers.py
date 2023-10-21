from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    # для того, щоб в автопарку відображались автомобілі з деталями
    # по конкретному серіалайзеру, а не лише з id
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at')
