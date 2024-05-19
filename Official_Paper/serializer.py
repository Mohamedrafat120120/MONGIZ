from rest_framework import serializers
from Official_Paper.models import paper

class papersSerializer(serializers.ModelSerializer):
    class Meta:
        model = paper
        fields = '__all__'