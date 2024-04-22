from django.shortcuts import render
from .models import Home_page
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import homeSerializer
from rest_framework.response import Response


@api_view(['POST','GET'])
def FBV_home(request):
    if request.method == 'GET':
        Home_page = Home_page.all()
        serializer = homeSerializer(Home_page)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = homeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

