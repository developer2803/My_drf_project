from rest_framework import viewsets

from .models import SubOrganization
from .serializers import SubOrganizationSerializer


class SubOrganizationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = SubOrganizationSerializer
    queryset = SubOrganization.objects.filter(published=True)
