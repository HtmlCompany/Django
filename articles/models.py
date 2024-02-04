from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self) -> str:
        return F"name = {self.name}"


class Article(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    text_article = models.CharField(max_length=5000, null=False)
    accept = models.BooleanField(default=False)
    date_of_publicate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return F"name = {self.name}"