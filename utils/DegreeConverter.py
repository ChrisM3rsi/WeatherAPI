def kelvinToCelcius(kelvin: float) -> float:
    return float('{0:.2f}'.format(kelvin - 273.15))


def kelvinToFahrenheit(kelvin: float) -> float:
    return float('{0:.2f}'.format(1.8 * kelvinToCelcius(kelvin) + 32))
