from django.http import HttpResponse
from django.shortcuts import render
from .models import Food_item

# Create your views here.
def foods_foods_views(request):
    foods = Food_item.objects.all().order_by('title')
    return render(request, 'foods/food.html', {'foods':foods})

def food_detail(request, slug):
    food = Food_item.objects.get(slug=slug)
    return render(request, 'foods/product_detail_f.html', {'food_detail':food})
