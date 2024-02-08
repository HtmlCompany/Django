from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategForm, ArticleText
from .models import Category, Article

# Create your views here.

def main(request):
    articles = Article.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'articles/index.html', {'articles': articles})

@login_required
def check(request, art_id):
    Article.objects.filter(pk=art_id, user=request.user).update(accept=True)
    return redirect(to='articles:main')

@login_required
def delete_article(request, art_id):
    Article.objects.get(pk=art_id, user=request.user).delete()
    return redirect(to='articles:main')

@login_required
def categories(request):
    if request.method == 'POST':
        form = CategForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
            return redirect(to='articles:main')
        else:
            return render(request, 'articles/categories.html', {'form': form})
    return render(request, 'articles/categories.html', {'form': CategForm()})

@login_required
def art(request):
    category = Category.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = ArticleText(request.POST)
        if form.is_valid():
            art_text = form.save(commit=False)
            art_text.user = request.user
            art_text.save()
            choice_cat = Category.objects.filter(name__in=request.POST.getlist('category'), user=request.user)
            for tag in choice_cat.iterator():
                art_text.tags.add(tag)
            return redirect(to='articles:index')
        else:
            return render(request, 'articles/art.html', {"category": category, 'form': form})
        
    return render(request, 'articles/art.html', {"category": category, 'form': ArticleText()})

@login_required
def detail(request, art_id):
    text = get_object_or_404(Article, pk=art_id, user=request.user)
    return render(request, 'articles/posts.html', {"text": text})

def page_not_found(request, exeption):
    return render(request, 'articles/404.html')