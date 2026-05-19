from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Про нас")],
        [KeyboardButton(text="Послуги")],
        [KeyboardButton(text="Залишити заявку")],
        [KeyboardButton(text="Контакти")],
        [KeyboardButton(text="Ціни")]
    ],
    resize_keyboard=True
)