from django import forms
from .models import Genre, Review

# from KinoVibe.utils import *

class MovieFilterForm(forms.Form):
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        required=False,
    )
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
    
class ReviewForm(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choises_rating, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
        

class TestForm(forms.Form):
    text = forms.CharField(max_length=40)
    text1 = forms.CharField(max_length=20)