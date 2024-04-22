from rest_framework import serializers
from Official_Paper.models import papers

class papersSerializer(serializers.ModelSerializer):
    class meta:
        model = papers
        fields = '__all__'