from rest_framework import viewsets

from ..models import News, Category
from .serializers import NewsSerializer, CategorySerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.
    """
    serializer_class = NewsSerializer
    queryset = News.objects.order_by('-created_at')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()