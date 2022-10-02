from utils.DegreeConverter import kelvinToFahrenheit, kelvinToCelcius
from django.db import IntegrityError
from history.models import Weather, WeatherStatistics
from utils.ApiKey import API_KEY
import requests
import datetime
import random
import logging
import statistics
def run():
    """
    This is the solution in case the API key was working fine.

    basic_url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
    date = datetime.datetime.today().timestamp()
    weather = []
    for i in range(10):
        params = {"lat": 40.629269, "lon": 22.947412, "dt": date, "appid": API_KEY}
        req = requests.get(basic_url, params=params)
        res = req.json()
        description = res['weather'][0]['description']
        temp = res['data'][0]['temp']
        data = {
                    'description': random.choice(dummy_description),
                    'temperature_Kelvin': temp,
                    'temperature_Celcius': kelvinToCelcius(temp),
                    'temperature_Fahrenheit': kelvinToFahrenheit(temp),
                    'date': datetime.date.fromtimestamp(date - i * 86400)
                }
        date = data['date']
        weather.append(data)

    rest code remains the same (line 56 and on)

    """

    dummy_description = ["clear sky", "raining", "windy", "snowing"]
    date = datetime.datetime.today().timestamp()
    weather = []
    temps_kelvin = []
    temps_celcius = []
    temps_fahrenheit = []
    for i in range(10):
        temp = random.randint(288, 298)
        data = {
            'description': random.choice(dummy_description),
            'temperature_Kelvin': temp,
            'temperature_Celcius': kelvinToCelcius(temp),
            'temperature_Fahrenheit': kelvinToFahrenheit(temp),
            'date': datetime.date.fromtimestamp(date - i * 86400)
        }
        temps_kelvin.append(data['temperature_Kelvin'])
        temps_celcius.append(data['temperature_Celcius'])
        temps_fahrenheit.append(data['temperature_Fahrenheit'])
        weather.append(data)
        try:
            q = Weather(description=data['description'], temp_kelvin=temp, temp_celcius=kelvinToCelcius(temp),
                        temp_fahrenheit=kelvinToFahrenheit(temp), date=datetime.date.fromtimestamp(date - i * 86400))
            q.save()
        except IntegrityError:
            logging.warning("duplicate entry, skipping...")
            continue

    mean_kelvin = statistics.mean(temps_kelvin)
    mean_celcius = statistics.mean(temps_celcius)
    mean_fahrenheit = statistics.mean(temps_fahrenheit)
    median_kelvin = statistics.median(temps_kelvin)
    median_celcius = statistics.median(temps_celcius)
    median_fahrenheit = statistics.median(temps_fahrenheit)

    q = WeatherStatistics(mean_kelvin=mean_kelvin, mean_celcius=mean_celcius,
                          mean_fahrenheit=mean_fahrenheit, median_kelvin=median_kelvin,
                          median_celcius=median_celcius, median_fahrenheit=median_fahrenheit)

    q.save()