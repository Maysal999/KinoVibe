# Generated by Django 5.1 on 2024-10-22 00:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('profile', models.ImageField(upload_to='actior/')),
                ('date_borth', models.DateField()),
                ('date_dead', models.DateField(default='01/01/2001', null=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Videofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('background_image', models.ImageField(null=True, upload_to='image')),
                ('video', models.FileField(null=True, upload_to='videos')),
                ('date', models.DateField(null=True, verbose_name='data_vypuska')),
                ('info', models.CharField(max_length=500)),
                ('actore', models.ManyToManyField(to='KinoVibe.actore', verbose_name='актеры')),
                ('genre', models.ManyToManyField(to='KinoVibe.genre', verbose_name='genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('assesment', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, verbose_name='Оценка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product', to='KinoVibe.videofile', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.AddField(
            model_name='actore',
            name='films',
            field=models.ManyToManyField(related_name='films', to='KinoVibe.videofile'),
        ),
    ]
