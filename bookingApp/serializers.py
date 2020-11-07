from . import models
from rest_framework  import serializers
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = (
			'username',
			'email'
		)

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Service
		fields = (
			'serviceTitle',
			'icon',
		)

class SubServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.SubService
		fields = (
			'service',
			'subServiceTitle',
		)

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Location
		fields = (
			'lat_lng',
			'houseNo',
			'description',
		)

class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Jobs
		fields = (
			'subService',
			'serviceProvider',
			'description',
			'price',
			'max_booking',
		)

class ServiceProviderSerializer(serializers.ModelSerializer):
	jobs_set = JobSerializer(many=True, read_only=False)

	class Meta:
		model = models.ServiceProvider
		fields = (
			'user',
			'photo',
			'is_online', 
			'phone', 
			'gender', 
			'workingRadius',
			'lat_lng',
			'jobs_set',
		)

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Customer
		fields=(
			'user',
			'photo',
			'is_online',
			'phone',
			'gender',
		)


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Order
		fields = (
			'serviceProvider',
			'customer',
			'deliveryAddress',
			'additionalRemark',
			'paymentType',
			'scheduleType',
			'scheduleDate',
			'orderStatus',
		)

class OrderDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.OrderDetails
		fields = (
			'order',
			'job',
			'price',
			'quantity',
		)