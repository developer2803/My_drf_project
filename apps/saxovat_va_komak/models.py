from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


class JamgarmaYili(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Saxovat va ko'mak jamgarmasi"
        verbose_name_plural = "Saxovat va ko'mak jamgarmalari"

class JamgarmaChoragi(models.IntegerChoices):
    FIRST = 1, "BIRINCHI CHORAK"
    SECOND = 2, "IKKINCHI CHORAK"
    THIRD = 3, "UCHINCHI CHORAK"
    FOURTH = 4, "TO'RTINCHI CHORAK"

class Jamgarma(models.Model):
    jamgarma_yili = models.ForeignKey(JamgarmaYili, related_name='jamgarmalar',  on_delete=models.CASCADE, verbose_name='Выбирите Jamgarma yili')
    jamgarma_choragi = models.IntegerField(choices=JamgarmaChoragi.choices, verbose_name='Выбирите четверть')
    image = models.ImageField(upload_to='news/%Y/%m/%d', verbose_name='Фото')
    title = models.CharField(max_length=250)
    description = RichTextUploadingField(verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Jamg'arma"
        verbose_name_plural = "Jamg'armalar"