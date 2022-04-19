from modeltranslation.translator import TranslationOptions, register

from .models import Ad, PressContact


@register(Ad)
class AdTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(PressContact)
class PressContactTranslationOptions(TranslationOptions):
    fields = ('fio', 'position')