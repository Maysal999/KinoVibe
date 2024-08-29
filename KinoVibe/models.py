from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.category}'
    
class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.genre}'
