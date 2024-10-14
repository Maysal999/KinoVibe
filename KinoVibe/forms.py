from django import forms
from .models import Genre

class MovieFilterForm(forms.Form):
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        required=False,
    )
    
    
class ReviewForm(forms.Form):
    class Meta:
        fields = ['text',"assesment"]

        