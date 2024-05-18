from rest_framework import serializers
from Health.models import health_state , medical_history

class healthstate_serializer(serializers.ModelSerializer):
    class Meta:
        model = health_state
        fields = '__all__'


class medicalhistory_serializer(serializers.ModelSerializer):
    class Meta:
        model = medical_history
        fields = '__all__'
