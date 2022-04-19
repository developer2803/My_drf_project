# Generated by Django 3.2 on 2022-04-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Региональный отдел', 'verbose_name_plural': 'Региональные отдели'},
        ),
        migrations.AddField(
            model_name='region',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]