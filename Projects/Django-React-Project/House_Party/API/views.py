from django.shortcuts import render
from .serializer import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CreateRoomSerializer(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        pass


