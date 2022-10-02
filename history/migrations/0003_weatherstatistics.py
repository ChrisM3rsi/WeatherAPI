# Generated by Django 4.1.1 on 2022-10-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0002_alter_weather_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeatherStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("mean_kelvin", models.FloatField()),
                ("mean_celcius", models.FloatField()),
                ("mean_fahrenheit", models.FloatField()),
                ("median_kelvin", models.FloatField()),
                ("median_celcius", models.FloatField()),
                ("median_fahrenheit", models.FloatField()),
            ],
        ),
    ]
