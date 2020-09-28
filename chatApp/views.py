from django.shortcuts import render
from . import models, serializers
from rest_framework import generics

# Create your views here.

class ListCreateChat(generics.ListCreateAPIView):
	queryset = models.Chat.objects.all()
	serializer_class = serializers.ChatSerializer

class RetrieveUpdateDestroyChat(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Chat.objects.all()
	serializer_class = serializers.ChatSerializer