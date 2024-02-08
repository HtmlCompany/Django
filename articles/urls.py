from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.categories, name='categories'),
    path('art/', views.art, name='art'),
    path('detail/<int:art_id>', views.detail, name='detail'),
    path('check/<int:art_id>', views.check, name='check'),
    path('delete_article/<int:art_id>', views.delete_article, name='delete_article'),
]
