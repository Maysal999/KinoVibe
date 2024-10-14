from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView


from .forms import MovieFilterForm
from .models import Category, Genre, Videofile
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
    return movie_genre

def index(request):
    categories = Genre.objects.all()
    video = Videofile.objects.all()
  
    context = {
        'categories':categories,
        'content' : video,
    }
    return render(request,'pages/index.html',context)

def category_filter(request,cat_id):
    category = Genre.objects.get(id=cat_id)  
    content = Videofile.objects.filter(genre=category)
    categories = Genre.objects.all()
    context = {
        'content' : content,
        'categories':categories,
    }
    return render(request,'pages/index.html',context)


class Category(ListView):
    template_name = 'pages/index.html'
    model = Videofile
    context_object_name = 'content'
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
class ShowView(DetailView):
    template_name = 'pages/show_video.html'
    context_object_name = 'movie'
    model = Videofile
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context =  super().get_context_data(**kwargs)  
    #     context['genre'] = Videofile.genre   

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