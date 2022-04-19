from rest_framework import serializers

from .models import Administration


class AdministrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Administration
        exclude = ['published']