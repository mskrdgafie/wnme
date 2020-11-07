from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status
from . import models
from . import serializers

from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Create your views here.
longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)

# service provider
class ListCreateServiceProvider(generics.ListCreateAPIView):
	queryset = models.ServiceProvider.objects.annotate(distance=Distance('lat_lng', user_location)).order_by('distance')
	serializer_class = serializers.ServiceProviderSerializer

class RetrieveUpdateDestroyServiceProvider(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.ServiceProvider.objects.all()
	serializer_class = serializers.ServiceProviderSerializer


# customer
class ListCreateCustomer(generics.ListCreateAPIView):
	queryset = models.Customer.objects.all()
	serializer_class = serializers.CustomerSerializer

class RetrieveUpdateDestroyCustomer(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Customer.objects.all()
	serializer_class = serializers.CustomerSerializer


# Jobs
class ListCreateJobs(generics.ListCreateAPIView):
	queryset = models.Jobs.objects.all()
	serializer_class = serializers.JobSerializer

class RetrieveUpdateDestroyJobs(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Jobs.objects.all()
	serializer_class = serializers.JobSerializer


#Order
class ListCreateOrder(generics.ListCreateAPIView):
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer

class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer


# OrderDetail
class ListCreateOrderDetail(generics.ListCreateAPIView):
	queryset = models.OrderDetails.objects.all()
	serializer_class = serializers.OrderDetailSerializer

class RetrieveUpdateDestroyOrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.OrderDetails.objects.all()
	serializer_class = serializers.OrderDetailSerializer


# service
class ListService(generics.ListAPIView):
	queryset = models.Service.objects.all()
	serializer_class = serializers.ServiceSerializer

class ListSubService(generics.ListAPIView):
	queryset = models.SubService.objects.all()
	serializer_class = serializers.SubServiceSerializer



