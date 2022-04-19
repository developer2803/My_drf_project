from modeltranslation.translator import TranslationOptions, register
from .models import CentralOffice

@register(CentralOffice)
class CentralOfficeTranslationOptions(TranslationOptions):
    fields = ('title', 'fullname', 'position', 'activity', 'obligation', 'bio')