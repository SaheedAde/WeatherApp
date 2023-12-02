from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    #This is the URL of my API
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3423e5de9500285fc637c6e8bf9be4da'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    #The City from the database
    city = City.objects.latest('id')

    form = CityForm()

    #request for the city_weather and convert the JSON to dictionary
    city_weather = requests.get(url.format(city)).json()

    if city_weather['cod']!='404':
        #This is the content to parse to templates
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
        }
    else:
        weather = {
            'message' : str(city)+' is not a valid city name! Enter a valid city name.',
        }
        City.objects.latest('id').delete()

    #pass weather content into context
    context = {'weather' : weather, 'form' : form }

    #This will return template
    return render(request, 'weather/index.html', context)
