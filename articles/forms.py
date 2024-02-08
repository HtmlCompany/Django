from django.forms import ModelForm, CharField, TextInput
from .models import Category, Article


class CategForm(ModelForm):

    name = CharField(min_length=3, max_length=32, required=True, widget=TextInput())
    
    class Meta:
        model = Category
        fields = ['name']


class ArticleText(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    text_article = CharField(min_length=10, max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Article
        fields = ['name', 'text_article']
        exclude = ['category']