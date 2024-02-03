from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse("<h1>Main page</h1>")

def categories(request, cat_id: int):
    if cat_id > 5:
        raise Http404()
    return HttpResponse(F"<h2>Categories</h2><p>category: {cat_id}</p>")

def page_not_found(request, exeption):
    return HttpResponseNotFound('404')