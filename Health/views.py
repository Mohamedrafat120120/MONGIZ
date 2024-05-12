from django.shortcuts import render
from .models import health_state,medical_history
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import healthstate_serializer, medicalhistory_serializer
from rest_framework.response import Response



@api_view(['GET'])
def FBV_health(request):
    if request.method == 'GET':
        health_state = health_state.all()
        serializer = healthstate_serializer(health_state,many=True)
        return Response(serializer.data)
