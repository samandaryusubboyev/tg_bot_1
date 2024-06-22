from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Sandan kottaman 😏", callback_data="option1")
button2 = InlineKeyboardButton(text="👈🏻  👉🏻", callback_data="option2")
button3 = InlineKeyboardButton(text="Sizdan kichkinaman 😢", callback_data="option3")
keyboard.add(button1, button2, button3)

