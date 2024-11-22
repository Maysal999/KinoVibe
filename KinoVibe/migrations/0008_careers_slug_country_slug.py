# Generated by Django 5.1 on 2024-10-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KinoVibe', '0007_personaj_borthman_personaj_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='careers',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(default='1', max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
