from rest_framework import viewsets

from .models import Administration
from .serializers import AdministrationSerializer


class AdministrationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = AdministrationSerializer
    # queryset = Administration.objects.all()
    queryset = Administration.objects.filter(published=True)
