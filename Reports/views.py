from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Reports.serialization import ReportSerializer
from rest_framework.response import Response
from .models import *

class Message(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user=request.user
        data=request.data
        serialize = ReportSerializer(data)
        if serialize.is_valid():
          Sender =Report.objects.create(Sender=user) 
          Sender.save()
          serialize.save()
          return Response(serialize.data,status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
      
    
