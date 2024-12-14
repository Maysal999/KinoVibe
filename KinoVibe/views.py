from itertools import product
from typing import Any

import requests
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,DetailView, CreateView
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# from .utils import movie_api

from .forms import  ReviewForm, TestForm
from .models import Category, Genre, Review, Videofile, UserAction
from .utils import search_filter
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
class CategoryListView(ListView):
    model = Category
    template_name = 'base.html'
    context_object_name = 'categories'


def get_all_totoly_context():
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return context
def get_genre(genre):
    movie_genre = Genre.objects.filter(genre__in=genre)
    return {"genress" : movie_genre}

def index(request):
    video = Videofile.objects.prefetch_related('genre')
    context = {
                'content' : video,
    }
    return render(request,'pages/index.html',context)
# @cache_page(15*60)
def category_filter(request,cat_slug):
    categories = Genre.objects.all()
    category = categories.get(slug=cat_slug)  
    content = Videofile.objects.filter(genre=category)
    context = {
        'content' : content,
        'categories':categories,
    }
    return render(request,'pages/index.html',context)

# @method_decorator(cache_page(60*15), name='dispatch')  # Кэшировать на 15 минут
class Category(ListView):
    template_name = 'pages/index.html'
    model = Videofile
    context_object_name = 'content'
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

#@method_decorator(cache_page(60*15), name='dispatch')  # Кэшировать на 15 минут
class ShowView(DetailView,CreateView):
    template_name = 'pages/show_video.html'
    context_object_name = 'movie'
    model = Videofile
    form_class = ReviewForm


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = context['movie'].title
        context['review'] = Review.objects.filter(movie__id=context['movie'].id)
        context['genress'] = Genre.objects.filter(videofile__id=context['movie'].id)
        return context

    
    
# @method_decorator(cache_page(60*15), name='dispatch')  # Кэшировать на 15 минут
class MovieFilterSearch(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'content'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        return context
    def get_queryset(self):
        movie = search_filter(self.request)
        return movie

class ReviewAddView(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'pages/show_video.html'

    def form_valid(self, form):
        if form.is_valid():
            # Получаем фильм по ID из формы
            movie = Videofile.objects.get(slug=form.data['movie'])
            
            # Рассчитываем новый рейтинг
            review_count = movie.review_movie.count()
            new_rating = (movie.rating * review_count + int(form.cleaned_data['assesment'])) / (review_count + 1)
            
            # Создаем и сохраняем отзыв
            review = form.save(commit=False)
            review.user_id = form.data['user']  # Присваиваем ID пользователя
            review.movie = movie  # Устанавливаем поле movie
            review.save()
            
            # Обновляем рейтинг фильма
            movie.rating = new_rating
            movie.save()

            # Перенаправляем обратно на страницу с фильмом
            return redirect('show_video', form.data['movie'])
        
        return HttpResponse('Неправильный запрос', status=400)
class FavoriteView(generic.ListView):
    context_object_name = 'action'
    model = UserAction
    template_name = 'pages/favorite.html'

# class MovieApiShowView(TemplateView):
#     template_name = 'pages/test_api.html'
#     context_object_name = 'movies'
#     api_secret = '5514eb7edaa910c57713f6391196ab48'
#     url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_secret}&language=en-US&page=1'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             response = requests.get(url=self.url)
#             data = response.json()
#             if response.status_code == 200:
#                 context['movie'] =
#         return context


