import requests
import os
from datetime import datetime
from pprint import pprint

# Variables
key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()

forecast_items = data['list']

for forecast in forecast_items:
    timestamp = forecast['dt'] #Unix timestamp
    date = datetime.fromtimestamp(timestamp) # Convert to a datetime, for humans
    temp = forecast['main']['temp']
    print(f'at{date} temp is {temp}')




