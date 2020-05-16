from django.shortcuts import render
from rest_framework import viewsets 
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
