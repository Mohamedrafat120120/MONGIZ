from django.shortcuts import render
from .models import health_state,medical_history
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import healthstate_serializer, medicalhistory_serializer
from rest_framework.response import Response



@api_view(['POST'])
def FBV_health(request):
    if request.method == 'POST':
        serializer = healthstate_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
