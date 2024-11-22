from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
from .utils import *

class Careers(models.Model):
    career = models.CharField(max_length=100,verbose_name="каьера")
    slug = models.SlugField(verbose_name='URL',unique=True,max_length=255,)
    class Meta:
        verbose_name="каьера"
        verbose_name_plural = "профессии"
    def __str__(self) -> str:
        return f'{self.career}'
    
class Country(models.Model):
    title_country = models.CharField(max_length=100,verbose_name="страны")
    slug = models.SlugField(verbose_name='URL',unique=True,max_length=255,)
    class Meta:
        verbose_name="страна"
        verbose_name_plural = "страны"
    def __str__(self) -> str:
        return f'{self.title_country}'
    

class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.category}'
    
class Genre(models.Model):
    genre = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='URL',unique=True,max_length=255,)
    def __str__(self) -> str:
        return f'{self.genre}'
    def get_absolute_url(self):
        
        return reverse('cat_id', kwargs={'cat_slug': self.slug})
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'




class Personaj(models.Model):
    fio = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name='URL',unique=True,max_length=255,)
    bio = models.TextField()
    profile = models.ImageField(upload_to='actior/')
    borthman = models.ManyToManyField('KinoVibe.Personaj',related_name='personaj',blank=True)
    career = models.ManyToManyField('KinoVibe.Careers',related_name='careers',blank=True)
    country = models.ManyToManyField('KinoVibe.Country',related_name='films',blank=True)
    date_borth = models.DateField()
    date_dead = models.DateField(blank=True, null=True)
    films = models.ManyToManyField('KinoVibe.Videofile',related_name='films',blank=True)
    genre = models.ManyToManyField('KinoVibe.Genre',verbose_name='genre')
    def __str__(self) -> str:
        return f'{self.fio}'
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
# class Review(models.Model):
#     comment = models.CharField(max_length=255)
#     star = models.CharField(max_length=3,choices=utils.choises_rating)

   
class Videofile(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='URL',unique=True,max_length=255,)
    background_image = models.ImageField(upload_to='image',null=True)
    video = models.FileField(upload_to='videos',null=True)
    country_1 = models.CharField(verbose_name='страны',choices=country,max_length=255)
    compositor = models.ManyToManyField('KinoVibe.Personaj',verbose_name='композитор',related_name='compositor_video')
    actores = models.ManyToManyField('KinoVibe.Personaj',verbose_name='актеры')
    screenwriter = models.ManyToManyField('KinoVibe.Personaj',verbose_name='Сценарист',related_name='screenwriter_movie')
    director = models.ManyToManyField('KinoVibe.Personaj',verbose_name='актеры',related_name='director')
    genre = models.ManyToManyField('KinoVibe.Genre',verbose_name='genre')
    date = models.DateField(verbose_name='data_vypuska', null=True)
    info = models.CharField(max_length=500)
    rating = models.DecimalField(verbose_name='рейтинг', default=0,decimal_places=1,max_digits=10)
    depth = 1

    class Meta:
        verbose_name = 'Кинофайл'
        verbose_name_plural = 'Кинофайлы'
    def __str__(self) -> str:
        return f'{self.title}'
    
    # def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
    #     self.slug = f"slugify{self.genre}/slugify{self.slug}"
    #     super().save(force_insert, force_update, using, update_fields)
    # def get_absolute_url(self):
        
    #     return reverse('cat_id', kwargs={'slug': self.slug,'country':self.country_1})

class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    assesment = models.CharField(verbose_name='Оценка', max_length=50, choices=choises_rating)
    movie = models.ForeignKey('KinoVibe.Videofile', on_delete=models.CASCADE, verbose_name='продукт',related_name='review_movie')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    created = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Reviews'

class UserAction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actions")
    video = models.ForeignKey(Videofile, on_delete=models.CASCADE, related_name="actions")
    is_favorite = models.BooleanField(default=False)
    watch_later = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'video')