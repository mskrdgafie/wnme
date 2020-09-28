from django.shortcuts import render
from . import models, serializers
from rest_framework import generics

# Create your views here.

class ListCreateRating(generics.ListCreateAPIView):
	queryset = models.Rating.objects.all()
	serializer_class = serializers.RatingSerializer

# on retrive and update delate rating
class RetrieveUpdateDestroyRating(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer