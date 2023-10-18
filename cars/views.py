from rest_framework.views import APIView
from .serializers import CarSerializer, CarsSerializer
from .filters import car_filtered_queryset


class CarListCreateView(APIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)
