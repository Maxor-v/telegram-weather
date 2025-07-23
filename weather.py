import requests
from config import API_KEY

def get_weather(city):
   api_key = API_KEY
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   response = requests.get(url)
   return response.json()