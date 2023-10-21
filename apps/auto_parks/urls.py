from django.urls import path

from apps.auto_parks.views import AutoParkListView, AutoParkCreateCarRetrieveCarsView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_parks_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkCreateCarRetrieveCarsView.as_view(), name='auto_parks_add_car')

]
