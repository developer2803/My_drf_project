from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Audio(models.Model):
    file = models.FileField(upload_to='audios/%Y/%m/%d', verbose_name="Файл")
    description = RichTextUploadingField(null=True, blank=True, verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")


    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"


class Video(models.Model):
    file = models.FileField(upload_to='videos/%Y/%m/%d', verbose_name="Файл")
    description = RichTextUploadingField(null=True, blank=True, verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name="Файл")
    description = RichTextUploadingField(null=True, blank=True, verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотография"
