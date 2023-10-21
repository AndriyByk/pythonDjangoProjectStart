from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response

from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserCreateAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()

        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)
