from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'drinks'

urlpatterns = [
    path('drinks/', views.foods_drinks_views, name="drinks"),
    re_path('drinks/(?P<slug>[\w-]+)/', views.drink_detail, name="ddetail"),
    re_path('(?P<drink_choice>[\w-]+)/', views.drink_filter, name="dsel"),
]