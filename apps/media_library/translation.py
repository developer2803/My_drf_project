from modeltranslation.translator import TranslationOptions, register

from .models import Audio, Video, Image


@register(Audio)
class AudioTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('description',)
