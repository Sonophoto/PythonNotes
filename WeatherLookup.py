#!/usr/bin/env python

import argparse
import sys

import requests
import requests.exceptions

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
    url = 'http://ip-api.com/json'

    r = requests.get(url)
    if (r):
        geodata = r.json()
        return geodata 
    return None


def fetch_local_weather(lat, lon, us_zip="", API_key=""):
    """
    Retrieve current weather from api.openweathermap.org.

    WARNING: Free API allows a maximum of 60 requests/minute
    Documentation: http://openweathermap.org/current#geo 
    Returns a dict decoded from the API's JSON response
    Returns 'None' if ANY errors occur, service is unavailable.
    """
    API_endpoint = 'http://api.openweathermap.org/data/2.5/weather' 
    API_key = '4a4446cce56aa27a6cd85eaa0e2bb7af' 
    our_params = dict(lat=lat, lon=lon, APPID=API_key)
        
    r = requests.get(API_endpoint, params=our_params)
    if (r):
        local_weather = r.json()
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
    API_endpoint = 'http://api.openweathermap.org/data/2.5/forecast' 
    API_key = '4a4446cce56aa27a6cd85eaa0e2bb7af' 
    our_params = dict(lat=lat, lon=lon, APPID=API_key)
   
    r = requests.get(API_endpoint, params=our_params)
    if (r):
        local_forecast = r.json()
        if local_forecast['cod'] == 200:
            return forecast_weather
    return None
    

def to_fahrenheit(celsius_temp):
    """convert celsius to degrees fahrenheit."""
    return 1.8 * (celsius_temp) + 32

def to_celsius(kelvin_temp):
    """convert kelvin to celsius."""
    return (kelvin_temp - 273.15)


if __name__ == '__main__':
    geodata = fetch_IP_geodata()
    if (geodata):
        print("Geo Data: ")
        print(geodata)
    else: 
        print("ERROR: Bad Local Weather Request: None")

    local_weather = fetch_local_weather(geodata['lat'], geodata['lon'])
    if (local_weather):
        print("Local Weather Data: ")
        print(local_weather)
    else: 
        print("ERROR: Bad Local Weather Request: None")
        
    local_forecast = fetch_local_forecast(geodata['lat'], geodata['lon'])
    if (local_forecast):
        print("Local Forecast Data: ")
        print(local_forecast)
    else: 
        print("ERROR: Bad Forecast Request: None")

