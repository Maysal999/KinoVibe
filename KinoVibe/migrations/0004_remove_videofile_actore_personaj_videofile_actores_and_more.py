# Generated by Django 5.1 on 2024-10-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KinoVibe', '0003_alter_actore_films'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videofile',
            name='actore',
        ),
        migrations.CreateModel(
            name='Personaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('profile', models.ImageField(upload_to='actior/')),
                ('career', models.CharField(choices=[('Актер', 'Актер'), ('актриса', 'актриса'), ('Гримёр', 'Гримёр'), ('Декоратор', 'Декоратор'), ('Звукорежиссер', 'Звукорежиссер'), ('Костюмер', 'Костюмер'), ('Режиссер-постановщик', 'Режиссер-постановщик'), ('Сценарист', 'Сценарист'), ('Хореограф', 'Хореограф'), ('модель', 'модель'), ('певец', 'певец')], max_length=255)),
                ('date_borth', models.DateField()),
                ('date_dead', models.DateField(blank=True, default='01/01/2001', null=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('films', models.ManyToManyField(blank=True, related_name='films', to='KinoVibe.videofile')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.AddField(
            model_name='videofile',
            name='actores',
            field=models.ManyToManyField(to='KinoVibe.personaj', verbose_name='актеры'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='director',
            field=models.ManyToManyField(related_name='director', to='KinoVibe.personaj', verbose_name='актеры'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='screenwriter',
            field=models.ManyToManyField(related_name='screenwriter_movie', to='KinoVibe.personaj', verbose_name='Сценарист'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='compositor',
            field=models.ManyToManyField(related_name='compositor_video', to='KinoVibe.personaj', verbose_name='композитор'),
        ),
        migrations.DeleteModel(
            name='Actore',
        ),
    ]
