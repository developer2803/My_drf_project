from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Region(models.Model):
    CHOICES = (
        ('toshkent_shahar', 'Toshkent sh'),
        ('andijon', 'Andijon v'),
        ('namangan', 'Namangan v'),
        ('fargona', 'Farg\'ona v'),
        ('toshkent_viloyati', 'Toshkent v'),
        ('sirdaryo', 'Sirdaryo v'),
        ('jizzax', 'Jizzax v'),
        ('samarqand', 'Samarqand v'),
        ('navoi', 'Navoi v'),
        ('qashqadaryo', 'Qashqadaryo v'),
        ('surxondaryo', 'Surxondaryo v'),
        ('buxoro', 'Buxoro v'),
        ('xorazm', 'Xorazm v'),
        ('qoraqalpogiston', 'Qoraqalpog\'iston R'),
    )
    name = models.CharField(max_length=100, choices=CHOICES, verbose_name="Выберите регион")
    image_for_display = models.ImageField(upload_to='region/%Y/%m/%d', verbose_name="Главная фото")
    image_for_director = models.ImageField(upload_to='region/%Y/%m/%d', verbose_name="Фото директора")
    subsection_name = models.CharField(max_length=255, verbose_name="Название регионалное отделение")
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    visiting_time = models.CharField(max_length=255, verbose_name="Приём (10:00-18:80)")
    email = models.EmailField(max_length=255, blank=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    bio = RichTextUploadingField(verbose_name="Биография")
    goal = RichTextUploadingField(verbose_name="Долж обязанности")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")


    def __str__(self):
        return self.subsection_name

    class Meta:
        verbose_name = "Региональный отдел"
        verbose_name_plural = "Региональные отдели"
