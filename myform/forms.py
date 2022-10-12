from django import forms
from .models import myForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = myForm

        fields = ['uname', 'title', 'description']
        labels = {'uname':'Full Name'}
