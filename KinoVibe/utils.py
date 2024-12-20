import requests

from typing import Union
choises_rating = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
)

def search_filter(request):
    from KinoVibe.models import Videofile
    
    key = str(request.GET.get('key'))
    movie = Videofile.objects.filter(title__icontains=key)
    return movie

country = (
    ("Алжир","Алжир"),
    ("Иордания","Иордания"),
    ("Кувейт","Кувейт"),
    ("Оман","Оман"),
    ("Буркина-Фасо","Буркина-Фасо"),
    ("Китай","Китай"),
    ("Малайзия","Малайзия"),
    ("Монголия","Монголия"),
    ("Австрия","Австрия"),
    ("Испания","Италия"),
    ("Казахстан","Казахстан"),
    ("Кыргызстан","Кыргызстан"),
    ("Таджикистан","Таджикистан"),
    ("Франция","Франция"),
    ("Хорватия","Хорватия"),
    ("Узбекистан","Узбекистан"),
)

careers = (
    ("Актер","Актер"),
    ("актриса","актриса"),
    ("Гримёр","Гримёр"),
    ("Декоратор","Декоратор"),
    ("Звукорежиссер","Звукорежиссер"),
    ("Костюмер","Костюмер"),
    ("Режиссер-постановщик","Режиссер-постановщик"),
    ("Сценарист","Сценарист"),
    ("Хореограф","Хореограф"),
    ("модель","модель"),
    ("певец","певец"),
)

# def movie_api( ):
#     api_secret = '5514eb7edaa910c57713f6391196ab48'
#     url = f'https://api.themoviedb.org/3/movie/popular?api_key=5514eb7edaa910c57713f6391196ab48&language=en-US&page=1'
#     response = requests.get(url)
#     data = response.json()
#     print(data)

