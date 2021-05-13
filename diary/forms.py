from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import BeerReview, BeerType

# Customization of pre-built register form
class NewUserForm(UserCreationForm):
    first_name = forms.CharField(help_text="Enter your first name here", required=True)
    last_name = forms.CharField(help_text="Enter your last name here (optional)", required=False)
    email = forms.EmailField(help_text="Enter your email here", required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Tuples for choices in forms
RATINGS = (
    ('1', 'very bad'),
    ('2', 'bad'),
    ('3', 'average'),
    ('4', 'good'),
    ('5', 'perfect')
)

FILTERED = (
        ('y', 'filtered'),
        ('n', 'unfiltered')
    )

COLOR_TYPES = (
    ('d', 'dark'),
    ('l', 'light')
)

class AddNewBeerReviewForm(forms.Form):
    beer_image = forms.URLField(
        max_length=2000, 
        widget=forms.URLInput(attrs={'placeholder':'Enter URL containing beer image (optional)'}), 
        required=False
    )
    beer_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Enter beer name'}),
        required=True
    )
    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), empty_label='Select beer type:', required=True)
    
    blank_choice = (('', 'Rate this beer:'),) 
    beer_rating = forms.ChoiceField(
        choices=blank_choice + RATINGS, 
        required=True
    )
    comments = forms.CharField(
        max_length=500, 
        widget=forms.TextInput(attrs={'placeholder':'Enter your comments (optional)'}),
        required=False
    )


class UpdateBeerReviewForm(forms.Form):
    beer_image = forms.URLField(required=False)
    beer_name = forms.CharField()
    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), empty_label=None)
    beer_rating = forms.ChoiceField(choices=RATINGS)
    comments = forms.CharField(max_length=500, required=False)

class SearchBeerForm(forms.Form):
    beer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter beer name to search'}), required=True)

class FilterReviewsForm(forms.Form):
    blank_choice_rating = (('', 'Filter by rating'),) 
    blank_choice_filtered = (('', 'Filter by filtered/unfiltered beer type'),)
    blank_choice_color = (('', 'Filter by beer type color'),)

    beer_type = forms.ModelChoiceField(
        queryset=BeerType.objects.all(), 
        empty_label='Filter by beer type',
        required=False
        )

    beer_type_filtered = forms.ChoiceField(choices=blank_choice_filtered + FILTERED, required=False)
    beer_type_color = forms.ChoiceField(choices=blank_choice_color + COLOR_TYPES, required=False)
    beer_rating = forms.ChoiceField(choices=blank_choice_rating + RATINGS, required=False)