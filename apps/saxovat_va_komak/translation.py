from modeltranslation.translator import TranslationOptions, register

from .models import Jamgarma, JamgarmaYili


@register(JamgarmaYili)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Jamgarma)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
