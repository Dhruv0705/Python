from django.urls import path
from .views import RoomView, CreateRoomSerializer

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomSerializer.as_view())
]