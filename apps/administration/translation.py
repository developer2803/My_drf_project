from modeltranslation.translator import TranslationOptions, register

from .models import Administration


@register(Administration)
class AdministrationTranslationOptions(TranslationOptions):
    fields = ('fio', 'position', 'bio', 'goal')
