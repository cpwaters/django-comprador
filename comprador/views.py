from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse('Home')
    return render(request, 'index.html')

def about_view(request):
    #return HttpResponse("About")
    return render(request, 'about.html')