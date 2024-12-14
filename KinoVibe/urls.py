from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import index, category_filter, ShowView, MovieFilterSearch, ReviewAddView, FavoriteView

from . import views
urlpatterns = [
    # path('index/',IndexView.as_view(),name='index'),
    # path('cat/',CategoryListView.as_view(),name='categories'),
    path('index/',index,name='index'),
    path('show/<slug:slug>//', ShowView.as_view(),name='show_video'),
    # re_path(r'^(?P<country>[\w\-]+)/(?P<slug>[\w\-]+)/$', ShowView.as_view(), name='show_video'),
    path('category/<slug:cat_slug>/',category_filter,name='cat_id'),
    path('movie/search/', MovieFilterSearch.as_view(), name='search'),
    path('movie/<slug:slug>/add_review/', ReviewAddView.as_view(), name='add_review'),
    path('movie/<int:pk>/favorite', FavoriteView.as_view(),name='favorite'),
    # path('test/', MovieApiShowView.as_view(),name='test')
   
]

    # path('movies/',movie_filter,name='movie_list'),



