from .models import BooksModel
from django import forms


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = '__all__'
