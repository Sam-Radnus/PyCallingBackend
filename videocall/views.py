from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
@api_view(['POST'])
def welcome(request):
    return JsonResponse({"Message":"Welcome to PyCalling Backend"})

