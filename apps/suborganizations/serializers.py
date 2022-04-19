from rest_framework import serializers

from .models import SubOrganization


class SubOrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubOrganization
        exclude = ['published']
