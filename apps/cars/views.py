from .models import CarModel
from .serializers import CarSerializer, CarsSerializer
from .filters import CarFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


class CarListView(ListAPIView):
    serializer_class = CarsSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
