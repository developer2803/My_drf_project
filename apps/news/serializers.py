from rest_framework import serializers

from .models import News


# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source="category.name", read_only=True)
    news_type_name = serializers.CharField(source='get_news_type_display', read_only=True)
    
    class Meta:
        model = News
        exclude = ['published']