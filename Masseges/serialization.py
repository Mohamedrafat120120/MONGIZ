from rest_framework import serializers
from .models import *
class MassegesSerialize(serializers.ModelSerializer):
    class Meta:
     model=masseges
     fields=("Issue",)