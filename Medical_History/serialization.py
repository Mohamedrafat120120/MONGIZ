from rest_framework import serializers
from .models import *

class medicalhistoryserialization(serializers.ModelSerializer):
    class Meta:
        model = medical_history
        fields='__all__'