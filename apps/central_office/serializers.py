from rest_framework import serializers
from .models import CentralOffice

class CentralOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralOffice
        exclude = ['published']