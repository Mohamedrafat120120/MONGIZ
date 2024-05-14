from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serialization import *
from .models import *
# Create your views here.
class personal_id_card(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
            data=request.data
            # user_id=request.user.id
            # user=get_object_or_404(User,pk=user_id)
            serialize=PersonalIDSerialization(data=data)
            if serialize.is_valid():
                # Sender=Personal_ID_Card.objects.create(user=user)
                # Sender.save()
                serialize.save()
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
               
class personal_driving_license(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
            data=request.data
            serialize=PersonalDrivingLicenseSerialization(data=data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
    
            