from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'nfi'

urlpatterns = [
    path('nfi/', views.foods_none_views, name="nfi"),
    re_path('nfi/(?P<slug>[\w-]+)/', views.none_detail, name="ndetail"), # Why wont this work if i use re_path ??
]