from rest_framework import viewsets

from .models import Ad, PressContact
from .serializers import AdSerializer, PressContactSerailizer


class AdViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Adds instances.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.order_by('-date').filter(published=True)


class PressContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing PressContacts instances
    """
    serializer_class = PressContactSerailizer
    queryset = PressContact.objects.filter(published=True)