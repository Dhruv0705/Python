from rest_framework import serializers
from .models import Room

def is_valid(self, *, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'Code', 'Host', 'GuestCanPause', 'VotesToSkip', 'CreatedAt')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields = ('GuestCanPause', 'VotesToSkip')
