from django import template

from KinoVibe.models import Genre, Videofile, Actore

register = template.Library()

@register.inclusion_tag('components/header/category.html')
def category():
    return {"genres" : Genre.objects.all()}
    


@register.simple_tag()
def genre_filter(movie_id:None):
    genres = Videofile.objects.get(title=movie_id).genre.all()
    return ', '.join([genre.genre for genre in genres])

@register.simple_tag(name='movie_actores1')
def movie_actores(movie_id:int)-> int:
    return movie_id


@register.simple_tag(name='movie_actores')
def actore_films(movie_id:int) -> int:
    actores = Videofile.objects.get(id=movie_id).actore.all()
    actore_list = []
    for a  in actores:
        actore = Actore.objects.get(fio=a)
        actore_list.append(actore)
    return  actore_list






