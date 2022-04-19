from modeltranslation.translator import TranslationOptions, register

from .models import News


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description')
