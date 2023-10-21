from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkCreateCarRetrieveCarsView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()

        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)

        park_serializer = AutoParkSerializer(auto_park)
        return Response(park_serializer.data, status.HTTP_201_CREATED)

    # непонятно як працювати з серіалайзером - які аргументи ставити
    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarSerializer(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


