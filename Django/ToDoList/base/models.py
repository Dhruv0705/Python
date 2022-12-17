from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    UserInformation = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank= True)
    Title = models.CharField(max_length=200)
    Description = models.TextField(null=True, blank=True)
    CompletedTask = models.BooleanField(default = False)
    CreatedTimeNDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
    
    class Meta:
        ordering = ['CompletedTask']