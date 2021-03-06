# Generated by Django 3.2 on 2022-04-01 04:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioChiqish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_oz', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('audio', models.FileField(upload_to='audios/%Y/%m/%d', verbose_name='Название')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Аудио выступления руководства',
                'verbose_name_plural': 'Аудио выступления руководства',
            },
        ),
        migrations.CreateModel(
            name='TextChiqish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_oz', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Текстовая  выступления руководства',
                'verbose_name_plural': 'Текстовые  выступления руководства',
            },
        ),
        migrations.CreateModel(
            name='VideoChiqish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_oz', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d', verbose_name='Видео')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Видео выступления руководства',
                'verbose_name_plural': 'Видео выступления руководства',
            },
        ),
    ]
