from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'weather_app/home.html')

def about(request):
    return render(request, "weather_app/about.html")

def index(request):
    if request.method =='POST':
        city=request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=6d6bfcbd36f7912a7b25984ba1423511').read()

        list_of_data = json.loads(source)
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']) + 'k',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            }
        print(data)
    else:
        data={}
    
    return render(request, "weather_app/index.html", data)
