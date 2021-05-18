from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

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