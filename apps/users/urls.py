from django.urls import path

from apps.users.views import UserListCreateView, UserRetrieveUpdateDestroyView, UserCreateAutoParkView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users-list-create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto-parks', UserCreateAutoParkView.as_view(), name='users_add_auto_park'),

]
