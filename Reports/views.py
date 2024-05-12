from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Reports.serialization import ReportSerializer
from rest_framework.response import Response

@api_view
@permission_classes((IsAuthenticated,))
def FBV_report(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
