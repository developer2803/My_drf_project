from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Ad(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    short_description = RichTextUploadingField(verbose_name="Краткое описание")
    description = RichTextUploadingField(verbose_name="Описание")
    image = models.ImageField(upload_to='ads/%Y/%m/%d', verbose_name="Рекламы")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class PressContact(models.Model):
    fio = models.CharField(max_length = 150, verbose_name='ФИО руководителя пресс-служба')
    image = models.ImageField(upload_to='press_contact/%Y/%m/%d', verbose_name='Фото руководителя')
    position = models.CharField(max_length = 150, verbose_name='Должность руководителя')
    email = models.EmailField()
    phone = models.CharField(max_length=15, verbose_name='Телефоне')
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Пресс-контакт"
        verbose_name_plural = "Пресс-контакти"

    def __str__(self):
        return self.fio
        