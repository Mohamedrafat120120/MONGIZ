from rest_framework import serializers
from .models import *
class ReportSerialize(serializers.ModelSerializer):
    class Meta:
     model=Report
     fields=("Issue",)