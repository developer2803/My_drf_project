from rest_framework import viewsets

from .models import Jamgarma, JamgarmaYili
from .serializers import JamgarmaSerializer, JamgarmaYiliSerializer


class JamgarmaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = JamgarmaSerializer
    queryset = Jamgarma.objects.order_by('jamgarma_yili').filter(published=True)


class JamgarmaYiliViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = JamgarmaYiliSerializer
    queryset = JamgarmaYili.objects.all()
