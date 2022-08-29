from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def welcome(request):
    return JsonResponse({"Message":"Welcome to PyCalling Backend"})