from rest_framework.decorators import api_view
from rest_framework import status
from Reports.serialization import ReportSerializer
from rest_framework.response import Response

@api_view
def FBV_report(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
