from django.urls import path
from .views import StationViewSet

station_list = StationViewSet.as_view({
    'post': 'create',
    'get': 'list',
})

urlpatterns = [
    path('stations/', station_list, name='station-list'),
    path('stations/<int:pk>/nearby/', StationViewSet.as_view({'get': 'nearby'}), name='station-nearby'),
]

