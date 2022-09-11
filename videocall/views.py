from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Participant,Hosts
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,authentication
from .serializers import ParticipantSerializer
# Create your views here.

def welcome(request):
    return JsonResponse({"Message":"Welcome to PyCalling Backend"})

@api_view(['POST'])
def joinRoom(request):
    data=request.data
    print(data)
    try:
        try:
            nm=data['name']
            print(nm)
            isHost=Hosts.objects.filter(name=nm)
            print(isHost)
            if not isHost:
               isAdmin=False
            else:   
               isAdmin=True
        except:
            print(data['name'])
            isAdmin=False    
        participant=Participant.objects.create(
                name=data['name'],
                room_Name=data['room_Name'],
                isAdmin=isAdmin,
                uid=data['uid']
        )
        serializer=ParticipantSerializer(participant,many=False)
        return Response(serializer.data)
    except:
        print(serializer.data)
        message={'detail':'User with this Name Already Exists'}    
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def leaveRoom(request,pk):
    participant=Participant.objects.get(uid=pk)
    participant.delete()
    return Response('Participant was deleted')

@api_view(['GET'])
def getParticipantInfo(request,pk,sk):
    try:
       participant=Participant.objects.get(uid=pk,room_Name=sk)
       serializer=ParticipantSerializer(participant,many=False)
       return JsonResponse(serializer.data)   
    except:
       message={'detail':'User with this UID does not Exist'}    
       return JsonResponse(message,status=status.HTTP_400_BAD_REQUEST)  

