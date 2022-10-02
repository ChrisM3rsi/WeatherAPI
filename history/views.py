import logging

from utils.DegreeConverter import kelvinToFahrenheit, kelvinToCelcius
from django.http import JsonResponse
from django.db import IntegrityError
from history.models import Weather, WeatherStatistics
from utils.ApiKey import API_KEY
import requests
import datetime
import random
import logging
import statistics


def history(request, timestamp):
    # this does not work due to API key error
    basic_url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
    params = {"lat": 40.629269, "lon": 22.947412, "dt": timestamp, "appid": API_KEY}
    req = requests.get(basic_url, params=params)
    res = req.json()
    description = res['weather'][0]['description']
    temp = res['data'][0]['temp']
    date = datetime.date.fromtimestamp(res['data'][0]['dt'])
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