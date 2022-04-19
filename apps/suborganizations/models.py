from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class SubOrganization(models.Model):
    image = models.ImageField(upload_to='sub_organizations/%Y/%m/%d', verbose_name="Фото")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextUploadingField(verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "подорганизация"
        verbose_name_plural = "Подорганизации"