from rest_framework import serializers
from Social.models import social_state , Family


class social_state_serializer(serializers.ModelSerializer):
    class Meta:
        model = social_state
        fields = '__all__'

class Family_serializer(serializers.ModelSerializer):
    class Meta:
        model= Family
        fields = '__all__'