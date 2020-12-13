from django.http import HttpResponse
from django.shortcuts import render
from .models import None_item

def foods_none_views(request):
    nfi = None_item.objects.all().order_by('title')
    return render(request, 'nfi/none_foods.html', {'nfi':nfi})

def none_detail(request, slug):
    none = None_item.objects.get(slug=slug)
    return render(request, 'nfi/product_detail_n.html', {'none_detail':none})