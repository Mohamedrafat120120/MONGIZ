from rest_framework import serializers
from Home.models import Home_page

class homeSerializer(serializers.ModelSerializer):
    class meta:
        model = Home_page
        fields ='__all__'
