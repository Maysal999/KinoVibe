from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
from . import utils
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.category}'
    
class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.genre}'
    def get_absolute_url(self):
        
        return reverse('cat_id', kwargs={'cat_id': self.pk})
class Actore(models.Model):
    fio = models.CharField(max_length=100)
    bio = models.TextField()
    profile = models.ImageField(upload_to='actior/')
    date_borth = models.DateField()
    date_dead = models.DateField(default='01/01/2001',null=True)
    films = models.ManyToManyField('KinoVibe.Videofile',related_name='films')

    def __str__(self) -> str:
        return f'{self.fio}'

# class Review(models.Model):
#     comment = models.CharField(max_length=255)
#     star = models.CharField(max_length=3,choices=utils.choises_rating)

   
class Videofile(models.Model):
    title = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='image',null=True)
    video = models.FileField(upload_to='videos',null=True)
    actore = models.ManyToManyField('KinoVibe.Actore',verbose_name='актеры')
    genre = models.ManyToManyField('KinoVibe.Genre',verbose_name='genre')
    date = models.DateField(verbose_name='data_vypuska', null=True)
    info = models.CharField(max_length=500)
    depth = 1

    
    def __str__(self) -> str:
        return f'{self.title}'

class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    assesment = models.CharField(verbose_name='Оценка', max_length=50, choices=utils.choises_rating)
    product = models.ForeignKey('KinoVibe.Videofile', on_delete=models.CASCADE, verbose_name='продукт',related_name='review_product')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    created = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
