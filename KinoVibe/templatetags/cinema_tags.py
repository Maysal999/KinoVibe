from django import template

from KinoVibe.models import Genre, Videofile, Personaj, Review

register = template.Library()

@register.inclusion_tag('components/header/category.html')
def category():
    return {"genres" : Genre.objects.all()}
    


@register.simple_tag()
def genre_filter(movie_id:None):
    genres = Videofile.objects.get(title=movie_id).genre.all()
    return [genre.genre for genre in genres]

@register.simple_tag(name='movie_actores1')
def movie_actores(movie_id:int)-> int:
    return movie_id


@register.simple_tag(name='movie_tags')
def actore_films(movie_id:int) -> int:
    movie = Videofile.objects.get(id=movie_id)
    actores = movie.actores.all()
    genres = movie.genre.all()
    actore_list = []
    genre_list = [genre.genre for genre in genres]
    for a  in actores:
        actore = Personaj.objects.get(fio=a)
        actore_list.append(actore)
    return {
        "actores" : actore_list,
        "genres" : genre_list
    }



@register.simple_tag()
def review_tag(movie_id):
    review = Review.objects.filter(movie_id=movie_id)
    return review


