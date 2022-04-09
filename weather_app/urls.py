from django.urls import path
from . import views

app_name='weather_app'
urlpatterns=[
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('get_any_city_weather_info_', views.index, name='index'),
]