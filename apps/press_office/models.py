from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class VideoChiqish(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    video = models.FileField(upload_to='videos/%Y/%m/%d', verbose_name='Видео')
    date = models.DateTimeField(verbose_name='Дата')
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео выступления руководства"
        verbose_name_plural = "Видео выступления руководства"

class AudioChiqish(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    audio = models.FileField(upload_to='audios/%Y/%m/%d', verbose_name='Название')
    date = models.DateTimeField(verbose_name='Дата')
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аудио выступления руководства"
        verbose_name_plural = "Аудио выступления руководства"


class TextChiqish(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Название')
    description = RichTextUploadingField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата')
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Текстовая  выступления руководства"
        verbose_name_plural = "Текстовые  выступления руководства"