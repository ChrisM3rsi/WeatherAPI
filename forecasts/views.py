import requests
from django.http import JsonResponse
import datetime
from utils.DegreeConverter import kelvinToFahrenheit, kelvinToCelcius
from utils.ApiKey import API_KEY




def current(request):
    basic_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": 40.629269, "lon": 22.947412, "appid": API_KEY}

    req = requests.get(basic_url, params=params)
    res = req.json()
    description = res['weather'][0]['description']
    temp = res['main']['temp']
    date = datetime.date.fromtimestamp(res['dt'])
    data = {
        'weather': {
            'description': description,
            'temperature_Kelvin': temp,
            'temperature_Celcius': kelvinToCelcius(temp),
            'temperature_Fahrenheit': kelvinToFahrenheit(temp),
            'date': date
        }
    }
    return JsonResponse(data)


def latest(request):
    basic_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"lat": 40.629269, "lon": 22.947412, "appid": API_KEY}

    req = requests.get(basic_url, params=params)
    res = req.json()
    description = res['list'][-1]['weather'][0]['description']
    temp = res['list'][-1]['main']['temp']
    date = datetime.date.fromtimestamp(res['list'][-1]['dt'])
    data = {
        'weather': {
            'description': description,
            'temperature_Kelvin': temp,
            'temperature_Celcius': kelvinToCelcius(temp),
            'temperature_Fahrenheit': kelvinToFahrenheit(temp),
            'date': date,
        }
    }
    return JsonResponse(data)
