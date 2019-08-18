import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8d8eb521cfe3ef7d22cc093b1de2f841'
    city = 'London'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    r = requests.get(url.format(city)).json()

    for city in cities:

        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            }

        weather_data.append(city_weather)

    print(weather_data)

    context = {
        'weather_data' : weather_data,
        'form' : form
    }

    return render(request, 'Weather/Weather.html', context)