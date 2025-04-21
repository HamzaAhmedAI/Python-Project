import requests
from pprint import pprint

API_Key = 'd8fa03d5389d5ff100dac0195d51ffef' 

city = input("Enter the city name: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}"

weather_data = requests.get(base_url).json()

pprint(weather_data)

