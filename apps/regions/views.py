from rest_framework import viewsets

from .models import Region
from .serializers import RegionSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = RegionSerializer
    queryset = Region.objects.filter(published=True)
