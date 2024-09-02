from django.db import models

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
    genre = models.ManyToManyField(Genre,verbose_name='genre')
    info = models.CharField(max_length=500)
    

    
    def __str__(self) -> str:
        return f'{self.title}'

