import logging
import asyncio
import g4f
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import nest_asyncio
nest_asyncio.apply()
TOKEN = '6122222610:AAFcGasSkJLYdjldRzv8Rkd6O-IStwHAFrs'

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()


def crtmsg(args):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": args}],
        provider=g4f.Provider.DeepAi)
    return response

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("test1"))
async def send(message : types.Message, command):
    await message.reply(crtmsg(command.args))



async def main():
    await dp.start_polling(bot)

asyncio.run(main())

# prompt = input()
# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": prompt}],
#     provider=g4f.Provider.DeepAi)
# print(response)
