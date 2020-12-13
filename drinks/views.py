from django.http import HttpResponse
from django.shortcuts import render
from .models import Ditem, Dcat

def foods_drinks_views(request):
    drinks = Ditem.objects.all().order_by('title')
    return render(request, 'drinks/drinks.html', {'drinks':drinks})

def drink_detail(request, slug):
    drink = Ditem.objects.get(slug=slug)
    return render(request, 'drinks/product_detail_d.html', {'drink_detail':drink})



def drink_select(request, drink_choice):
    dc = Dcat.objects.get()
    return render(request, 'drinks/drinks.html', {'dc':dc})



def drink_filter(request, drink_choice):
    choice = request.GET.get('selector')
    item = Ditem.objects.all()
    cat = Dcat.objects.all()
    if choice == cat:
       return render(request, 'drinks/filtered_drinks.html', {'selecteds':selecteds})
    else:
        return render(request, 'drinks/drinks.html')
