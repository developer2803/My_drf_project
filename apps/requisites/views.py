from rest_framework import viewsets

from .models import Requisite
from .serializers import RequisiteSerializer


class RequisiteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = RequisiteSerializer
    queryset = Requisite.objects.filter(published=True)
