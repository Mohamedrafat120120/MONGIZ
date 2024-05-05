from django.shortcuts import render
from .models import message
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import msg_serializer
from rest_framework.response import Response


@api_view(['GET'])
def FBV_msg(request):
    if request.method == 'GET':
        message = message.all()
        serializer = msg_serializer(message, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
