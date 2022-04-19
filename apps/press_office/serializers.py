from rest_framework import serializers
from .models import VideoChiqish, AudioChiqish, TextChiqish

class AudioChiqishSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioChiqish
        exclude = ['published']

class VideoChiqishSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoChiqish
        exclude = ['published']

class TextChiqishSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextChiqish
        exclude = ['published']
