from .models import CarModel
from .serializers import CarSerializer, CarsSerializer
from .filters import car_filtered_queryset
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


class CarListView(ListAPIView):
    serializer_class = CarsSerializer
    queryset = CarModel.objects.all()
    #
    # def get_queryset(self):
    #     return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
