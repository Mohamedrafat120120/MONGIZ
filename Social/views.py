from django.shortcuts import render
from .models import social_state
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import social_state_serializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def FBV_social(request):
    if request.method == 'GET':
        social_state = social_state.all()
        serializer = social_state_serializer(social_state)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = social_state_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

