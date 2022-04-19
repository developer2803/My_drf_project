from rest_framework import serializers

from ..models import News, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    news_type_name = serializers.CharField(source='get_news_type_display', read_only=True)
    
    class Meta:
        model = News
        fields = ['id', 'category', 'category_name', 'title', 'short_description', 'description', 'news_type', 'news_type_name',
            'date', 'img', 'created_at', 'updated_at']