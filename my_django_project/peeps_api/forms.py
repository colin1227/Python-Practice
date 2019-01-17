from django import forms
from .models import People

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('first_name','last_name','age','birth_year', 'birth_month', 'birth_day')