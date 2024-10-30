from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Station

class StationTests(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(name="Station 1", latitude=40.7128, longitude=-74.0060)
        self.station2 = Station.objects.create(name="Station 2", latitude=40.7138, longitude=-74.0065)
        self.station3 = Station.objects.create(name="Station 3", latitude=40.7150, longitude=-74.0070)
        
    def test_create_station(self):
        url = reverse('station-list')
        data = {"name": "New Station", "latitude": 40.7129, "longitude": -74.0061}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Station.objects.count(), 4)
    
    def test_list_stations(self):
        url = reverse('station-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_nearby_station(self):
        url = reverse('station-nearby', args=[self.station1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Station 2")