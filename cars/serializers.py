from rest_framework import serializers

from cars.models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()

    seats = serializers.IntegerField()
    cab_type = serializers.CharField(max_length=20)
    volume = serializers.FloatField()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class CarsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()
