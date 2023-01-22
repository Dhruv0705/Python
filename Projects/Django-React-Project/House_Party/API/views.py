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

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):
        from .models import Room
        
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
            Guest_Can_Pause = serializer.data.get('Guest_Can_Pause')
            Votes_To_Skip = serializer.data.get('Votes_To_Skip')
            Host = self.request.session.session_key
            queryset = Room.objects.filter(Host=Host)
            if queryset.exists():
                room = queryset[0]
                room.Guest_Can_Pause = Guest_Can_Pause
                room.Votes_To_Skip = Votes_To_Skip
                room.save(update_fields=['Guest_Can_Pause', 'Votes_To_Skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(Host=Host, Guest_Can_Pause=Guest_Can_Pause, Votes_To_Skip=Votes_To_Skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


