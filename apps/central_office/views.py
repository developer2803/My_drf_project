from rest_framework import viewsets
from .models import CentralOffice
from .serializers import CentralOfficeSerializer


class CentralOfficeViewSet(viewsets.ModelViewSet):


    serializer_class = CentralOfficeSerializer
    queryset = CentralOffice.objects.filter(published=True)
