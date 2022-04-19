# Generated by Django 3.2 on 2022-03-26 19:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentralOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='central_office/%Y/%m/%d', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_oz', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('fullname', models.CharField(max_length=255, verbose_name='ФИО')),
                ('fullname_ru', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('fullname_en', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('fullname_uz', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('fullname_oz', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('position_ru', models.CharField(max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(max_length=255, null=True, verbose_name='Должность')),
                ('position_uz', models.CharField(max_length=255, null=True, verbose_name='Должность')),
                ('position_oz', models.CharField(max_length=255, null=True, verbose_name='Должность')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('activity', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Деятельность')),
                ('activity_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Деятельность')),
                ('activity_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Деятельность')),
                ('activity_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Деятельность')),
                ('activity_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Деятельность')),
                ('obligation', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Обязательство')),
                ('obligation_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Обязательство')),
                ('obligation_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Обязательство')),
                ('obligation_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Обязательство')),
                ('obligation_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Обязательство')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Биография')),
                ('bio_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Биография')),
                ('bio_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Биография')),
                ('bio_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Биография')),
                ('bio_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Биография')),
            ],
            options={
                'verbose_name': 'Центральный аппарат',
                'verbose_name_plural': 'Центральные аппарат',
            },
        ),
    ]
