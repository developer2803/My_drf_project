# Generated by Django 3.2 on 2022-04-04 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saxovat_va_komak', '0002_auto_20220401_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamgarma',
            name='jamgarma_yili',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jamgarmalar', to='saxovat_va_komak.jamgarmayili', verbose_name='Выбирите Jamgarma yili'),
        ),
    ]
