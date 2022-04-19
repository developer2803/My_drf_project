from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import SubOrganization


@admin.register(SubOrganization)
class SubOrganizationAdmin(TranslationAdmin):
    list_display = ('title', 'published')
    list_editable = ('published', )
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
