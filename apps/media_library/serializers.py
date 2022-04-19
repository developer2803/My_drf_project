from rest_framework import serializers

from .models import Audio, Video, Image


class AudioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Audio
        exclude = ['published']

    
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        exclude = ['published']


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        exclude = ['published']