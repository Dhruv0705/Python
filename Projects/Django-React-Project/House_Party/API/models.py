from django.db import models
import string
import random

# Create your models here.
def GenerateUniqueCode():
    Length = 6

    while True:
        Code = ''.join(random.choices(string.ascii_uppercase, k=Length))
        if Room.objects.filter(Code=Code).count() == 0:
            break
    
    return Code

class Room(models.Model):
    Code = models.CharField(max_length=8, default="", unique=True)
    Host = models.CharField(max_length=50, unique=True)
    GuestCanPause = models.BooleanField(null=False, default=False)
    VotesToSkip = models.IntegerField(null=False, default=1)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    