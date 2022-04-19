from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# class Category(models.Model):
#     name = models.CharField("Название", max_length=255)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"


class NewsType(models.IntegerChoices):
    UZB = 1, "uzbekistan"
    FOND = 2, "fond_yangiliklari"
    WORLD = 3, "WORLD NEWS"
    SAXOVAT = 4, "savohat"



class News(models.Model):
    img = models.ImageField("Фотография", upload_to='news/%Y/%m/%d')
    title = models.CharField("Название", max_length=255)
    description = RichTextUploadingField(verbose_name="Описание")
    short_description = models.CharField("Короткое описание", max_length=500)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    news_type = models.IntegerField(choices=NewsType.choices, verbose_name="Тип")
    date = models.DateTimeField("Дата")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"