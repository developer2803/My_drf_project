from django.db import models


class UsefulLink(models.Model):
    logo = models.ImageField(upload_to='logos/%Y/%m/%d', verbose_name="Логотип")
    link = models.CharField(max_length=500, verbose_name="Ссылка")
    title = models.CharField(max_length=255, verbose_name="Название")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Полезная ссылка"
        verbose_name_plural = "Полезные ссылки"
