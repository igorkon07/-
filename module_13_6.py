from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api =''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Расчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.insert(button2)
lkb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
lkb.add(button1)
lkb.insert(button2)

class  UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Расчитать')
async def r_bot(message):
    await message.answer('Выберите опцию:', reply_markup=lkb)

@dp.callback_query_handler(text='formulas')
async def f_bot(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

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
    await message.answer('Привет!', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)