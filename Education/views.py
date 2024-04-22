from django.shortcuts import render
from .models import educational_state, certification
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import educational_state_serializer, certification_serializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def FBV_education(request):
    if request.method == 'GET':
        educational_state = educational_state.all()
        serializer = educational_state_serializer(educational_state, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = educational_state_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
