from django.forms import ModelForm, CharField, TextInput
from .models import Category


class CategForm(ModelForm):

    name = CharField(min_length=3, max_length=32, required=True, widget=TextInput())
    
    class Meta:
        model = Category
        fields = ['name']