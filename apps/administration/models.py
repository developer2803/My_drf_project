from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Administration(models.Model):
    image = models.ImageField(upload_to='adminstration/%Y/%m/%d', verbose_name="Фото")
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    visiting_time = models.CharField(max_length=255, verbose_name="Приём (10:00-18:00)")
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    bio = RichTextUploadingField(verbose_name="Биография")
    goal = RichTextUploadingField(verbose_name="Долж обязанности")

    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководства"
