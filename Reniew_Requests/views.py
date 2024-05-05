from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serialization import *
from .models import *
# Create your views here.
class personal_id_card(APIView):
    def post (self,request):
            data=request.data
            serialize=PersonalIDSerialization(data=data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
               
class personal_driving_license(APIView):
    def post (self,request):
            data=request.data
            serialize=PersonalDrivingLicenseSerialization(data=data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                   return Response(serialize.errors,status=status.HTTP_403_FORBIDDEN)
    
            