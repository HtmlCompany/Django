from django.shortcuts import render, redirect
# from forms import CategForm

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def categories(request):
    if request.method == 'POST':
        form = CategForm(request.POST)
        if form.is_valid():
            return redirect(to='articles:index')
        else:
            return render(request, 'articles/categories.html', {'form': form})
    return render(request, 'articles/categories.html', {'form': CategForm()})

def page_not_found(request, exeption):
    return render(request, 'articles/404.html')