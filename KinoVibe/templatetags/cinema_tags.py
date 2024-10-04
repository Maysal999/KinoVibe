from django import template

from KinoVibe.models import Genre

register = template.Library()

@register.inclusion_tag('components/header/category.html')
def category():
    return {"genres" : Genre.objects.all()}
    