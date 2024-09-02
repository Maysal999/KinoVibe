from django.urls import path

from .views import IndexView, CategoryListView, index

urlpatterns = [
    # path('index/',IndexView.as_view(),name='index'),
    # path('cat/',CategoryListView.as_view(),name='categories'),
    path('index/',index,name='index')

]

