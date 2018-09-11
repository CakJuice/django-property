from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(600)
def homepage(request):
    return render(request, 'base/homepage.html', locals())
