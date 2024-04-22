from django.shortcuts import render
from Official_Paper.models import papers
from rest_framework.decorators import api_view
from rest_framework import status
from Official_Paper.serializer import papersSerializer
from rest_framework.response import Response


@api_view([ 'GET'])
def FBV_paper(request):
    if request.method == 'GET':
        papers = papers.all()
        serializer = papersSerializer(papers)
        return Response(serializer.data)
