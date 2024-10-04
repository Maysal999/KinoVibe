from django.db import models
from django.urls import reverse
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
    genre = models.ManyToManyField('KinoVibe.Genre',verbose_name='genre')
    date = models.DateField(verbose_name='data_vypuska', null=True)
    info = models.CharField(max_length=500)
    depth = 1

    
    def __str__(self) -> str:
        return f'{self.title}'

