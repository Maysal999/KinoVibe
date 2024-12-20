# Generated by Django 5.1 on 2024-10-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KinoVibe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actore',
            options={'verbose_name': 'Актер', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='videofile',
            options={'verbose_name': 'Кинофайл', 'verbose_name_plural': 'Кинофайлы'},
        ),
        migrations.AddField(
            model_name='videofile',
            name='compositor',
            field=models.ManyToManyField(related_name='compositor_video', to='KinoVibe.actore', verbose_name='композитор'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='country_1',
            field=models.CharField(choices=[('Алжир', 'Алжир'), ('Иордания', 'Иордания'), ('Кувейт', 'Кувейт'), ('Оман', 'Оман'), ('Буркина-Фасо', 'Буркина-Фасо'), ('Китай', 'Китай'), ('Малайзия', 'Малайзия'), ('Монголия', 'Монголия'), ('Австрия', 'Австрия'), ('Испания', 'Италия'), ('Казахстан', 'Казахстан'), ('Кыргызстан', 'Кыргызстан'), ('Таджикистан', 'Таджикистан'), ('Франция', 'Франция'), ('Хорватия', 'Хорватия'), ('Узбекистан', 'Узбекистан')], default='2', max_length=255, verbose_name='страны'),
            preserve_default=False,
        ),
    ]
