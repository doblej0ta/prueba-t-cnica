from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Station
from .serializers import StationSerializer
import math

class StationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def nearby(self, request, pk=None):
        station = get_object_or_404(Station, pk=pk)
        
        def haversine(lat1, lon1, lat2, lon2):
            # Radio de la Tierra en kilómetros
            R = 6371.0
            # Conversión de grados a radianes
            lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return R * c

        # Calcular la estación más cercana manualmente
        closest_station = None
        min_distance = float('inf')
        
        for other_station in Station.objects.exclude(pk=pk):
            distance = haversine(
                station.latitude, station.longitude,
                other_station.latitude, other_station.longitude
            )
            if distance < min_distance:
                min_distance = distance
                closest_station = other_station

        if closest_station:
            serializer = StationSerializer(closest_station)
            return Response(serializer.data)
        
        return Response({"error": "No nearby station found"}, status=status.HTTP_404_NOT_FOUND)
