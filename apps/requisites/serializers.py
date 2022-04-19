from rest_framework import serializers

from .models import Requisite


class RequisiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Requisite
        exclude = ['published']
