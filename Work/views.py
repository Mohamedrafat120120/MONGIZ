from django.shortcuts import get_object_or_404
from .models import work_career
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Work.serializer import WorkSerializer
from rest_framework.response import Response

class work(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        data['Sender']=user.pk
        serializer=WorkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data sent","data":serializer.data},status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class get_work(APIView):
        permission_classes=[IsAuthenticated]     
        def get(self,request):
            user=request.user
            data=get_object_or_404(work_career,Sender=user)
            serialize=WorkSerializer(data)
            return Response(serialize.data,status=status.HTTP_200_OK)
             
        
