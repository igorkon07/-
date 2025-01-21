from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api =''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class  UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def fsm_handler(message, state):
    await state.update_data(age=message.text)
    dta = await state.get_data()
    #await message.answer(f'Ваш возраст {dta["age"]}')
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def fsm_handler(message, state):
    await state.update_data(growth=message.text)
    dta = await state.get_data()
    #await message.answer(f'Ваш рост {dta["growth"]}')
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def fsm_handler(message, state):
    await state.update_data(weight=message.text)
    dta = await state.get_data()
    #await message.answer(f'Ваш вес {dta["weight"]}')
    #для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    norm = 10*int(dta["weight"])+6.25*int(dta["growth"])-5*int(dta["age"])+5
    await message.answer(f'Ваша норма калорий {norm}')
    await state.finish()

@dp.message_handler(commands='start')
async def bot_start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer('Введите команду /start чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)