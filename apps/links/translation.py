from modeltranslation.translator import TranslationOptions, register

from .models import UsefulLink


@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ('title',)
