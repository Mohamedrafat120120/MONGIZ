from django.shortcuts import render,get_object_or_404
from .models import health_state,medical_history
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import healthstate_serializer, medicalhistory_serializer
from rest_framework.response import Response



class Health_State(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,national_id):
        data = get_object_or_404(health_state,pk=national_id)
        serialize = healthstate_serializer(data)
        return Response(serialize.data,status=status.HTTP_200_OK)
