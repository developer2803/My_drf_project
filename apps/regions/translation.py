from modeltranslation.translator import TranslationOptions, register

from .models import Region


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('subsection_name', 'fio', 'address', 'bio', 'goal')
