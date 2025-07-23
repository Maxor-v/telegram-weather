import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import TOKEN
from weather import get_weather

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/weather")


@dp.message(Command('weather'))
async def weather(message: Message):
    weather_data = get_weather("Paris")

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

    await message.answer(weather_message)


@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())