from modeltranslation.translator import TranslationOptions, register

from .models import SubOrganization


@register(SubOrganization)
class SubOrganizationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
