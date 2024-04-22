from django.shortcuts import render
from .models import work_career
from rest_framework.decorators import api_view
from rest_framework import status
from Work.serializer import WorkSerializer
from rest_framework.response import Response

@api_view
def FBV_work(request):
    if request.method == 'GET':
        work_career = work_career.all()
        serializer = WorkSerializer(work_career)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
