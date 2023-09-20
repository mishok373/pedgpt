import asyncio
import logging
import g4f
import nest_asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import Router
from aiogram.filters import Command

nest_asyncio.apply()
TOKEN = '122222610:AAFcGasSkJLYdjldRzv8Rkd6O-IStwHAFrs'

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

loop = asyncio.new_event_loop()
async def crtmsg(args):
    provider = g4f.Provider.DeepAi
    response = provider.create_async(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": args}])
    return response


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Разраб даун, так что если чтото (не)работает(не так) пишите этому аутисту: @mishok_373\nДоступные команды:\n/start(выводит это говно)\n/t *ваш_запрос*  (основная команда, создающая запрос)")

@dp.message(Command("t"))
async def cmd_t(message : types.Message, command):
    if command.args is not None:
        await message.reply('Думаю...')
        await message.reply(str(await asyncio.run(crtmsg(command.args))))
    else:
        await message.reply('!вы не вели запрос, либо он слишком короток')


# router = Router()
# @router.message()
# async def aanswer(message : types.message):
#     await message.reply('Думаю...')
#     await message.reply(str(await asyncio.run(crtmsg(message))))

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
