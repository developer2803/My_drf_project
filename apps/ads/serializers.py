from rest_framework import serializers

from .models import Ad, PressContact


class AdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        exclude = ['published']


class PressContactSerailizer(serializers.ModelSerializer):

    class Meta:
        model = PressContact
        exclude = ['published']
