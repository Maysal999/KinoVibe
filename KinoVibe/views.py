from django.views.generic import ListView,TemplateView


from .models import Category
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
class CategoryListView(ListView):
    model = Category
    template_name = "components/tools/category.html"
    context_object_name = 'categories'
