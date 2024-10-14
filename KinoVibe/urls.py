from django.urls import path

from .views import  index, category_filter, ShowView, MovieFilterSearch

urlpatterns = [
    # path('index/',IndexView.as_view(),name='index'),
    # path('cat/',CategoryListView.as_view(),name='categories'),
    path('index/',index,name='index'),
    path('show/<int:pk>/',ShowView.as_view(),name='show_video'),
    path('category/<int:cat_id>/',category_filter,name='cat_id'),
    path('movie/search/', MovieFilterSearch.as_view(), name='search'),
    # path('movies/',movie_filter,name='movie_list'),

]

