from django import forms
from django.forms import ModelChoiceField

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import BeerReview, BeerType

class AddNewBeerReviewForm(forms.Form):
    beer_image = forms.URLField(max_length=2000, help_text='Enter URL for beer image')
    beer_name = forms.CharField(help_text='Enter beer name')

    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), help_text='Choose a beer type')

    RATINGS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'average'),
        ('4', 'good'),
        ('5', 'perfect')
    )

    beer_rating = forms.ChoiceField(choices=RATINGS, help_text='Choose beer rating')
    comments = forms.CharField(max_length=500, help_text='Enter your additional comments concerning this beer')


class UpdateBeerReviewForm(forms.Form):
    beer_image = forms.URLField(help_text='Enter URL for beer image')
    beer_name = forms.CharField(help_text='Enter beer name')

    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), empty_label=None, help_text='Choose a beer type')

    RATINGS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'average'),
        ('4', 'good'),
        ('5', 'perfect')
    )

    beer_rating = forms.ChoiceField(choices=RATINGS, help_text='Choose beer rating')
    comments = forms.CharField(max_length=500, help_text='Enter your additional comments concerning this beer')