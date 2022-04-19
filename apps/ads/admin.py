from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Ad, PressContact


@admin.register(Ad)
class AdAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'published')
    list_editable = ('published', )
    search_fields = ('title', 'date')
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

@admin.register(PressContact)
class PressContactAdmin(TranslationAdmin):
    list_display = ('fio', 'position', 'phone', 'email', 'published')
    list_editable = ('published',)
    search_fields = ('fio', 'position')
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
