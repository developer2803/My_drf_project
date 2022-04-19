from rest_framework import serializers

from .models import Jamgarma, JamgarmaYili


class JamgarmaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Jamgarma
        fields = ['jamgarma_choragi', 'image', 'title', 'description', 'date']

class JamgarmaYiliSerializer(serializers.ModelSerializer):
    jamgarmalar = JamgarmaSerializer(many=True, read_only=True)

    class Meta:
        model = JamgarmaYili
        fields = ['name', 'jamgarmalar']


