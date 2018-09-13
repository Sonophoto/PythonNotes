import requests

"""
Communications library for commercial (COTS) USB weather stations:
https://github.com/jim-easterbrook/pywws/

Docs on adding your weather station to openweathermap.org:
http://openweathermap.org/stations
"""

def fetch_IP_geodata():
    """
    Retrieve geo data keyed by our IP address from ip-api.com.


    WARNING: API will block any IP doing 150+ requests/minute. 
    If blocked, visit http://ip-api.com/docs/unban
    Documentation: http://ip-api.com/docs/api:json
    Returns a dict decoded from the API's JSON response
    Returns 'None' if ANY errors occur, service is unavailable.
    """
    API_URL = 'http://ip-api.com/json'

    response = requests.get(API_URL)
    if (response):
        geodata = response.json()
        return geodata 
    return None


def fetch_local_weather(lat, lon, API_key=""):
    """
    Retrieve current weather from api.openweathermap.org.

    WARNING: Free API allows a maximum of 60 requests/minute
    Documentation: http://openweathermap.org/current#geo 
    Returns a dict decoded from the API's JSON response
    Returns 'None' if ANY errors occur, service is unavailable.
    """
    API_URL = 'http://api.openweathermap.org/data/2.5/weather'
    API_KEY ='e5591c0f23cf2f87b7854d06192b36af'
    local_params = dict(lat=lat, lon=lon, APPID=API_KEY)

    response = requests.get(API_URL, params=local_params)
    if (response):
        local_weather = response.json()
        if local_weather['cod'] == 200:
            return local_weather
    return None 
   

def fetch_local_forecast(lat, lon, us_zip="", API_key=""):
    """
    Retrieve 5 day forecast from api.openweathermap.org.

    Documentation: http://openweathermap.org/forecast5
    Returns a dict decoded from the API's JSON response
    Returns 'None' if ANY errors occur, service is unavailable.
    """
    API_URL = 'http://api.openweathermap.org/data/2.5/forecast'
    API_KEY = 'e5591c0f23cf2f87b7854d06192b36af'
    local_params = dict(lat=lat, lon=lon, APPID=API_KEY)

    response = requests.get(API_URL, params=local_params)
    if (response):
        local_forecast = response.json()
        #TODO We need to find the schema for this data and test 'cod' == 200
        if (local_forecast):
            return local_forecast
    return None
   

def to_fahrenheit(celsius_temp):
    """convert celsius to degrees fahrenheit."""
    return 1.8 * (celsius_temp) + 32

def to_celsius(kelvin_temp):
    """convert kelvin to celsius."""
    return (kelvin_temp - 273.15)


if __name__ == '__main__':
    # Do some Tests:
    # Grab our network connection's geographic data:
    geodata = fetch_IP_geodata()
    if (geodata):
        print("Geo Data: ")
        print(geodata)
    else: 
        print("ERROR: Bad Geo Data Request: None")

    # Now lets use our geodata to get some local weather information:
    local_weather = fetch_local_weather(geodata['lat'], geodata['lon'])
    if (local_weather):
        print("Local Weather Data: ")
        print(local_weather)
    else: 
        print("ERROR: Bad Local Weather Request: None")
    
    # Next lets use our geodata to get the 5-day forecast:
    local_forecast = fetch_local_forecast(geodata['lat'], geodata['lon'])
    if (local_forecast):
        print("Local Forecast Data: ")
        print(local_forecast)
    else: 
        print("ERROR: Bad Forecast Request: None")
