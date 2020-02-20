import requests
import pprint
import os
from datetime import datetime

domain = 'http://api.openweathermap.org'
# path = '/data/2.5/weather?' # current weather
path = '/data/2.5/forecast?' # forecast 
us_imperial = '&units=imperial&appid='
pp = pprint.PrettyPrinter(indent=4)

# api_key = '4fd9bdb77225b13451398b0f4fb73c5c'
# api_key = '69ba1d57027e9c667005ea7ac45b3dab'
key = os.environ.get('api_key')

# country_name = input('Enter the country you want to see the weather: ').lower()
# city_name = input('Enter the city you want to see the weather: ').lower()

country_name = 'us'
city_name = 'minneapolis'


query_parameters = f'q={city_name},{country_name}{us_imperial}{key}'

url = f'{domain}{path}{query_parameters}'

weather_data = requests.get(url).json()
# print('\n**Todays Temperature**')
# print(f'\n  Max Temp: {weather_data["main"]["temp_max"]}')
# print(f"  Min Temp: {weather_data['main']['temp_min']}")

data = 




