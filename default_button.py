from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Mening biografiyam"), KeyboardButton("<Taxsil olgan joylarim>")]
        ],
    resize_keyboard=True)

menu_education = ReplyKeyboardMarkup([
    [KeyboardButton("Maktab"), KeyboardButton("Litsey")],
    [KeyboardButton("Universitet"), KeyboardButton("O'quv kurslari"), KeyboardButton("Back")]
],
    resize_keyboard=True)


menu_courses = ReplyKeyboardMarkup([
    [KeyboardButton("Everest"), KeyboardButton("Cambridge"), KeyboardButton("Najot Ta'lim"), KeyboardButton("Back")]
],
    resize_keyboard=True)
