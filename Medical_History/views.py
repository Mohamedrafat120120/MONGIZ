from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serialization import *
from .models import * 
# Create your views here.

class medical_history(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data = get_object_or_404(medical_history,User=user)
        serialize = medicalhistory_serializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
