# Generated by Django 3.2 on 2022-04-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_library', '0002_auto_20220408_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
    ]
