from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'foods'

urlpatterns = [
    path('foods/', views.foods_foods_views, name="foods"),
    re_path('foods/(?P<slug>[\w-]+)/', views.food_detail, name="fdetail"),
]
