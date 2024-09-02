from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView


from .models import Category, Videofile
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
class CategoryListView(ListView):
    model = Category
    template_name = 'base.html'
    context_object_name = 'categories'

# def get_all_totoly_context(request):
#     categories = Category.objects.all()
#     context = {
#         'categories':categories
#     }
#     return render(request,'pages/index.html',context)
 

def index(request):
    categories = Category.objects.all()
    video = Videofile.objects.all()
    context = {
        'categories':categories,
        'content' : video
    }
    return render(request,'pages/index.html',context)

# class IndexView(ListView):
#     queryset = Videofile.objects.all()
#     context_object_name = 'content'
#     template_name = 'pages/index.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context =  super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()