from django.contrib import admin
from .models import VideoChiqish, AudioChiqish, TextChiqish
from modeltranslation.admin import TranslationAdmin

@admin.register(VideoChiqish)
class VideoChiqishAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'published')
    list_editable = ('published',)
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

@admin.register(AudioChiqish)
class AudioChiqishAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'published')
    list_editable = ('published',)
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

@admin.register(TextChiqish)
class TextChiqishAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'published')
    list_editable = ('published',)
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
