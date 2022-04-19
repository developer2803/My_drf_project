from django.db import models

from apps.regions.models import Region


class Requisite(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name="Регион")
    stir = models.CharField(max_length=255, verbose_name="ИНН")
    bank_name = models.CharField(max_length=255, verbose_name="Название банка")
    card_number_uzs = models.CharField(max_length=255, verbose_name="Номер карта uzs")
    card_number_usd = models.CharField(max_length=255, verbose_name="Номер карта uzd")
    card_number_eur = models.CharField(max_length=255, verbose_name="Номер карта eur")
    district_name = models.CharField(max_length=255, verbose_name="Город")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Реквизит"
        verbose_name_plural = "Реквизиты"
