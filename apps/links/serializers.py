from rest_framework import serializers

from .models import UsefulLink


class UsefulLinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UsefulLink
        exclude = ['published']