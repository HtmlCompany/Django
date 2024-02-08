from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategForm, ArticleText
from .models import Category, Article

# Create your views here.

def main(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def check(request, art_id):
    Article.objects.filter(pk=art_id).update(accept=True)
    return redirect(to='articles:main')

def delete_article(request, art_id):
    Article.objects.get(pk=art_id).delete()
    return redirect(to='articles:main')

def categories(request):
    if request.method == 'POST':
        form = CategForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='articles:main')
        else:
            return render(request, 'articles/categories.html', {'form': form})
    return render(request, 'articles/categories.html', {'form': CategForm()})

def art(request):
    category = Category.objects.all()

    if request.method == 'POST':
        form = ArticleText(request.POST)
        if form.is_valid():
            art_text = form.save()

            choice_cat = Category.objects.filter(name__in=request.POST.getlist('category'))
            for tag in choice_cat.iterator():
                art_text.tags.add(tag)
            return redirect(to='articles:index')
        else:
            return render(request, 'articles/art.html', {"category": category, 'form': form})
        
    return render(request, 'articles/art.html', {"category": category, 'form': ArticleText()})

def detail(request, art_id):
    text = get_object_or_404(Article, pk=art_id)
    return render(request, 'articles/posts.html', {"text": text})

def page_not_found(request, exeption):
    return render(request, 'articles/404.html')