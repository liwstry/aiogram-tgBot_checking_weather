import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.config import TOKEN

from func.get_data import get_data

bot = Bot(token=TOKEN)
db = Dispatcher()

@db.message(CommandStart())
# Define an asynchronous function called start that takes a parameter called message of type Message
async def start(message: Message):
    # Reply to the message with the text "Выберите город:"
    await message.reply("Выберите город:")

@db.message()
# Define an asynchronous function called data_weather that takes a Message object as an argument
async def data_weather(message: Message):
    # Get the text from the Message object
    city = message.text
    # Call the get_data function with the city as an argument
    weather_data = get_data(city)
    # If the weather_data is not empty
    if weather_data:
        # Reply to the Message object with the weather_data
        await message.reply(weather_data)


# Define an asynchronous function called main
async def main():   
    # Start polling the database for updates and pass the bot as an argument
    await db.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())