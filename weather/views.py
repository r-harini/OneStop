from django.shortcuts import render
import requests
from .models import City
from decouple import config
from .forms import CityForm

# Create your views here.
def index(request):
    url = config('WEATHER_API_URL')
    cities=City.objects.all() #return all the cities in the database
    
    if request.method== 'POST':
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    
    #city = 'Kolkata'
    form= CityForm()
    weather_data=[]

    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form': form}


    return render(request, 'weather/weather.html', context) #returns index.html template
