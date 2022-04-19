from rest_framework import viewsets

from .models import AudioChiqish, VideoChiqish, TextChiqish
from .serializers import AudioChiqishSerializer, VideoChiqishSerializer, TextChiqishSerializer


class AudioChiqishViewSet(viewsets.ModelViewSet):
    """
    A viewSet for viewing and editing audio matbuot
    """
    serializer_class = AudioChiqishSerializer
    queryset = AudioChiqish.objects.order_by('-date').filter(published=True)

class VideoChiqishViewSet(viewsets.ModelViewSet):
    """
    A viewSet for viewing and editing video maatbuot
    """

    serializer_class = VideoChiqishSerializer
    queryset = VideoChiqish.objects.order_by('-date').filter(published=True)

class TextChiqishViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing text matbuot
    """

    serializer_class = TextChiqishSerializer
    queryset = TextChiqish.objects.order_by('-date').filter(published=True)
