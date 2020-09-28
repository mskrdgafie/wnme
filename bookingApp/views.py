from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status
from . import models
from . import serializers

# Create your views here.


# service provider
class ListCreateServiceProvider(generics.ListCreateAPIView):
	queryset = models.ServiceProvider.objects.all()
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



