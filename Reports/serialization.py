from rest_framework import serializers
from Reports.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class meta:
        model = Report
        fields = '__all__'