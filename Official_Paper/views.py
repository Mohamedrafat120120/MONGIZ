from django.shortcuts import get_object_or_404
from Official_Paper.models import paper
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from Official_Paper.serializer import papersSerializer
from rest_framework.response import Response


class offcial_papers(APIView):
       permission_classes=[IsAuthenticated]
       def get(self,request):
          user=request.user
          Message =get_object_or_404(paper,User=user) 
          serializer = papersSerializer(Message)
          Id_Image=serializer.data.get('Id_Card')
          Id_Card_url='https://mongiz.pythonanywhere.com/'+Id_Image
          Birth_cirtification_image=serializer.data.get('Birth_cirtification')
          Birth_cirtification_url='https://mongiz.pythonanywhere.com/'+Birth_cirtification_image
          Passport_image=serializer.data.get('Passport')
          Passport_url='https://mongiz.pythonanywhere.com/'+Passport_image
          Driving_Licence_image=serializer.data.get('Driving_Licence')
          Driving_Licence_url='https://mongiz.pythonanywhere.com/'+Driving_Licence_image
          return Response({'Id_Card_url':Id_Card_url,'Birth_cirtification_url':Birth_cirtification_url,'Passport_url':Passport_url,'Driving_Licence_url':Driving_Licence_url},status=status.HTTP_200_OK)
