from django.shortcuts import render
from django.http import JsonResponse
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
        from .models import Room
        
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
            GuestCanPause = serializer.data.get('GuestCanPause')
            VotesToSkip = serializer.data.get('VotesToSkip')
            Host = self.request.session.session_key
            queryset = Room.objects.filter(Host=Host)
            if queryset.exists():
                Room = queryset[0]
                Room.GuestCanPause = GuestCanPause
                Room.VotesToSkip = VotesToSkip
                Room.save(update_fields=['GuestCanPause', 'VotesToSkip'])
            else:
                Room = Room(Host=Host, GuestCanPause=GuestCanPause, VotesToSkip=VotesToSkip)
                Room.save()
            
            return Response(RoomSerializer(Room).data, status=status.HTTP_200_OK)


