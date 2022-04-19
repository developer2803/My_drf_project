# Generated by Django 3.2 on 2022-04-01 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saxovat_va_komak', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jamgarma',
            options={'verbose_name': "Jamg'arma", 'verbose_name_plural': "Jamg'armalar"},
        ),
        migrations.AlterModelOptions(
            name='jamgarmayili',
            options={'verbose_name': "Saxovat va ko'mak jamgarmasi", 'verbose_name_plural': "Saxovat va ko'mak jamgarmalari"},
        ),
        migrations.RemoveField(
            model_name='jamgarma',
            name='created',
        ),
        migrations.RemoveField(
            model_name='jamgarma',
            name='updated',
        ),
        migrations.AddField(
            model_name='jamgarma',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]
