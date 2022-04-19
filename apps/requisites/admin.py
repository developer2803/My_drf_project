from django.contrib import admin

from .models import Requisite


@admin.register(Requisite)
class RequisiteAdmin(admin.ModelAdmin):
    list_display = ('stir', 'bank_name', 'district_name', 'published')
    list_editable = ('published', )
    search_fields = ('stir', 'district_name')
    list_filter = ('region', )
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
