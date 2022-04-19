from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class CentralOffice(models.Model):
    image = models.ImageField(upload_to='central_office/%Y/%m/%d', verbose_name="Фото")
    title = models.CharField(max_length=255, verbose_name="Название")
    fullname = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Email")
    activity = RichTextUploadingField(verbose_name="Деятельность")
    obligation = RichTextUploadingField(verbose_name="Обязательство")
    bio = RichTextUploadingField(verbose_name="Биография")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Центральный аппарат"
        verbose_name_plural = "Центральные аппарат"