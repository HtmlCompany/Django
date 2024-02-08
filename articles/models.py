from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self) -> str:
        return F"name = {self.name}"


class Article(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    text_article = models.CharField(max_length=5000, null=False)
    accept = models.BooleanField(default=False)
    date_of_publicate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return F"name = {self.name}"