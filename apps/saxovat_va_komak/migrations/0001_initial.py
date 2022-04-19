# Generated by Django 3.2 on 2022-03-27 15:22

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JamgarmaYili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_uz', models.CharField(max_length=250, null=True)),
                ('name_oz', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jamgarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jamgarma_choragi', models.IntegerField(choices=[(1, 'BIRINCHI CHORAK'), (2, 'IKKINCHI CHORAK'), (3, 'UCHINCHI CHORAK'), (4, "TO'RTINCHI CHORAK")], verbose_name='Выбирите четверть')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d', verbose_name='Фото')),
                ('title', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('title_uz', models.CharField(max_length=250, null=True)),
                ('title_oz', models.CharField(max_length=250, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('jamgarma_yili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saxovat_va_komak.jamgarmayili', verbose_name='')),
            ],
        ),
    ]
