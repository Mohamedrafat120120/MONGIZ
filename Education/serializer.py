from rest_framework import serializers
from Education.models import educational_state , certification

class educational_state_serializer(serializers.ModelSerializer):
    class meta:
        model = educational_state 
        fields = '__all__'
    

class certification_serializer(serializers.ModelSerializer):
    class meta:
        model = certification
        fields = '__all__'