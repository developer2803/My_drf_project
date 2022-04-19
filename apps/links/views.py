from rest_framework import viewsets

from .models import UsefulLink
from .serializers import UsefulLinkSerializer


class UsefulLinkViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = UsefulLinkSerializer
    queryset = UsefulLink.objects.filter(published=True)
