from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkWithoutCarsSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithoutCarsSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'auto_parks')
