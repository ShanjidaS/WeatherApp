import requests
from django.shortcuts import render

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8d8eb521cfe3ef7d22cc093b1de2f841'
    city = 'Amsterdam'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    return render(request, 'Weather/Weather.html', context)