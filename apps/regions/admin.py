from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Region


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ('subsection_name', 'fio', 'email', 'phone', 'published')
    list_editable = ('published', )
    search_fields = ('subsection_name',)
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