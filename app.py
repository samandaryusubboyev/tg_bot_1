#main.py module
import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_education, menu_courses
from inline_button import keyboard
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = "API_TOKEN"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_1 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursandman  {ful_name}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {ful_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mening biografiyam")
async def show_menu(message: types.Message):
    await message.answer("Mening to'liq ismim Yusubboyev Samandar. 2006-yil 23-mart sanasida Toshkent viloyatida tug'ilganman. Sizdan katta yoki kichik ekanligimni belgilab keting:) ", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "<Taxsil olgan joylarim>")
async def show_menu_1(message: types.Message):
    await message.answer("<Taxsil olgan joylarim>", reply_markup=menu_education)


@dp.message_handler(lambda message: message.text == "Maktab")
async def show_menu_2(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Qibray tumani Yangi avlod mahallasida joylashgan 31-sonli maktabda 2012-2021-yillar oralig'ida taxsil olganman!", reply_markup=menu_education)



@dp.message_handler(lambda message: message.text == "Litsey")
async def show_menu_3(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Toshkent Davlat Agrar Universiteti qoshida akademik litseyning Iqtisodiyot yo'nalishi bo'yicha 2021-2023-yillarda taxsil olib tamomladim!", reply_markup=menu_education)

@dp.message_handler(lambda message: message.text == "Universitet")
async def show_menu_4(message: types.Message):
    await message.answer("2023-yil Toshkent Axborot Texnologiyalari Universitetining Iqtisodiyot va menejment fakultetiga qabul qilindim!", reply_markup=menu_education)

@dp.message_handler(lambda message: message.text == "O'quv kurslari")
async def show_menu_5(message: types.Message):
    await message.answer("Kurslardan birini tanlang!", reply_markup=menu_courses)

@dp.message_handler(lambda message: message.text == "Everest")
async def show_menu_5(message: types.Message):
    await message.answer("Ingliz tilini o'rganishni Everest o'quv markazida boshladim va u yerda 3 oy mobaynida taxsil oldim!", reply_markup=menu_courses)


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu_6(message: types.Message):
    await message.answer("Back", reply_markup=menu_keyboard)



@dp.message_handler(lambda message: message.text == "Cambridge")
async def show_menu_7(message: types.Message):
    await message.answer("Cambridge o'quv markaziga borganimda pre-intermediate guruhiga qo'shildim va u yerda IELTS leveliga qadar o'qidim!", reply_markup=menu_courses)


@dp.message_handler(lambda message: message.text == "Najot Ta'lim")
async def show_menu_6(message: types.Message):
    await message.answer("Najot Ta'lim o'quv markazida Universitetga qabul qilinganimdan so'ng O'qishni boshladim va hozirgacha taxsil olib kelayapman! (2024-yil)", reply_markup=menu_courses)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
