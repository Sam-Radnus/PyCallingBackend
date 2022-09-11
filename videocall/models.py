from django.db import models

# Create your models here.
class Participant(models.Model):
    name=models.CharField(blank=False,max_length=100)
    uid=models.CharField(blank=False,max_length=200)
    room_Name=models.CharField(blank=False,max_length=200)
    joinedAt=models.TimeField(auto_now_add=True,editable=False)
    isAdmin=models.BooleanField(blank=True,default=False)
    cameraOn=models.BooleanField(default=True)
    micOn=models.BooleanField(default=True)
    screenOn=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    name=models.CharField(blank=False,max_length=200)
    user=models.ForeignKey(Participant,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Hosts(models.Model):
    name=models.CharField(blank=False,max_length=100)
    isAdmin=models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)