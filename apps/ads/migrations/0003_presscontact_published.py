# Generated by Django 3.2 on 2022-04-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_presscontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='presscontact',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]