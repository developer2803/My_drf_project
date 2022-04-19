from rest_framework import viewsets

from .models import Audio, Video, Image
from .serializers import AudioSerializer, VideoSerializer, ImageSerializer


class AudioViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = AudioSerializer
    queryset = Audio.objects.order_by('-date').filter(published=True)


class VideoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = VideoSerializer
    queryset = Video.objects.order_by('-date').filter(published=True)



class ImageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = ImageSerializer
    queryset = Image.objects.order_by('-date').filter(published=True)
