from rest_framework import serializers
from .models import *

class medicalhistory_serializer(serializers.ModelSerializer):
    class Meta:
        model = medical_history
        fields = '__all__'