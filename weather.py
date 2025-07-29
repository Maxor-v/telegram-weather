import requests
from config import API_KEY

def get_weather(city):
   api_key = API_KEY
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   response = requests.get(url)
   weather_data = response.json()

   if weather_data and weather_data.get('cod') == 200:
      # Извлечение данных
      city = weather_data['name']
      temp = weather_data['main']['temp']
      feels_like = weather_data['main']['feels_like']
      description = weather_data['weather'][0]['description'].capitalize()
      humidity = weather_data['main']['humidity']
      wind_speed = weather_data['wind']['speed']
      pressure = weather_data['main']['pressure']

      # Форматирование сообщения
      weather_message = (
         f"🌤 Погода в {city}:\n"
         f"▫️ Температура: {temp:.1f}°C (ощущается как {feels_like:.1f}°C)\n"
         f"▫️ Состояние: {description}\n"
         f"▫️ Влажность: {humidity}%\n"
         f"▫️ Ветер: {wind_speed} м/с\n"
         f"▫️ Давление: {pressure} гПа"
      )
   else:
      weather_message = "Не удалось получить данные о погоде."

   return weather_message