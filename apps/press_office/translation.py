from modeltranslation.translator import TranslationOptions, register
from .models import VideoChiqish, AudioChiqish, TextChiqish

@register(VideoChiqish)
class VideoChiqishTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(AudioChiqish)
class AudioChiqishTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(TextChiqish)
class TextChiqishTranslationOptions(TranslationOptions):
    fields = ('title', 'description')