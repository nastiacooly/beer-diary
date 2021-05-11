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


# Tuples for rating choices in forms
RATINGS = (
    ('1', 'very bad'),
    ('2', 'bad'),
    ('3', 'average'),
    ('4', 'good'),
    ('5', 'perfect')
)

class AddNewBeerReviewForm(forms.Form):
    beer_image = forms.URLField(max_length=2000, help_text='Enter URL for beer image', required=True)
    beer_name = forms.CharField(help_text='Enter beer name', required=True)
    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), help_text='Choose a beer type', required=True)
    beer_rating = forms.ChoiceField(choices=RATINGS, help_text='Choose beer rating', required=True)
    comments = forms.CharField(max_length=500, help_text='Enter your additional comments concerning this beer')


class UpdateBeerReviewForm(forms.Form):
    beer_image = forms.URLField(help_text='Enter URL for beer image')
    beer_name = forms.CharField(help_text='Enter beer name')
    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), empty_label=None, help_text='Choose a beer type')
    beer_rating = forms.ChoiceField(choices=RATINGS, help_text='Choose beer rating')
    comments = forms.CharField(max_length=500, help_text='Enter your additional comments concerning this beer')

class SearchBeerForm(forms.Form):
    beer_name = forms.CharField(help_text='Enter beer name for search', required=True)

class FilterReviewsForm(forms.Form):
    blank_choice = (('', '---------'),) 

    beer_type = forms.ModelChoiceField(queryset=BeerType.objects.all(), help_text='Choose a beer type', required=False)
    beer_rating = forms.ChoiceField(choices=blank_choice + RATINGS, help_text='Choose beer rating', required=False)