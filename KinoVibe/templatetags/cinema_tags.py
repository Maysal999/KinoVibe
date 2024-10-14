from django import template

from KinoVibe.models import Genre, Videofile

register = template.Library()

@register.inclusion_tag('components/header/category.html')
def category():
    return {"genres" : Genre.objects.all()}
    


@register.simple_tag()
def genre_filter(movie_id:None):
    genres = Videofile.objects.get(title=movie_id).genre.all()
    return ', '.join([genre.genre for genre in genres])

