from django.db import models
from django.db.models import constraints
from django.utils import timezone


class Weather(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    temp_kelvin = models.FloatField()
    temp_celcius = models.FloatField()
    temp_fahrenheit = models.FloatField()
    date = models.DateTimeField(unique=True)
    description = models.CharField(max_length=100)

    def get_date(self):
        return self.date


class WeatherStatistics(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    mean_kelvin = models.FloatField()
    mean_celcius = models.FloatField()
    mean_fahrenheit = models.FloatField()
    median_kelvin = models.FloatField()
    median_celcius = models.FloatField()
    median_fahrenheit = models.FloatField()
