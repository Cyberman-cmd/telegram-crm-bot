import os
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command


import database
from keyboards.menu import main_menu
from states.form import Form

router = Router()



@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привіт! Це твій перший бот 🚀",
        reply_markup=main_menu
    )

@router.message(lambda message: message.text == "Про нас")
async def about_handler(message: Message):
    await message.answer(
        "Ми створюємо Telegram ботів ⚡"
    )

@router.message(lambda message: message.text == "Послуги")
async def services_handler(message: Message):
    await message.answer(
        "Наші послуги:\n"
        "- Telegram боти\n"
        "- AI інтеграції\n"
        "- Автоматизація"
    )

@router.message(lambda message: message.text == "Контакти")
async def contacts_handler(message: Message):
    await message.answer(
        "@your_username"
    )

@router.message(lambda message: message.text == "Ціни")
async def prices(message: Message):
    await message.answer(
        "Ціни на наші послуги:\n"
        "- Telegram боти: 5000 грн\n"
        "- AI інтеграції: 10000 грн\n"
        "- Автоматизація: 15000 грн"
    )

# Початок заявки
@router.message(lambda message: message.text == "Залишити заявку")
async def form_start(message: Message, state: FSMContext):
    await state.set_state(Form.name)

    await message.answer(
        "Введіть ваше ім'я:"
    )

# Отримання імені
@router.message(Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Form.phone)

    await message.answer(
        "Введіть номер телефону:"
    )

# Отримання телефону
@router.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Form.email)
    await message.answer(
        "Введіть вашу електронну пошту:"
    )
@router.message(Form.email)
async def get_email(message: Message, state: FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer(
            "Будь ласка, введіть коректну електронну пошту:"
        )
        return
    lower_email = message.text.lower()
    await state.update_data(email=lower_email)
    await state.set_state(Form.comment)
    await message.answer(
        "Введіть коментар до заявки:"
    )
# Отримання коментаря
@router.message(Form.comment)
async def get_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)

    data = await state.get_data()
    name = data['name']
    phone = data['phone']
    email = data['email']
    comment= data['comment']

    database.add_new(
    name,
    phone,
    email,
    comment    
    )

    

    await message.answer(
        "Заявку відправлено ✅",
        reply_markup=main_menu
    )


    

    bot = message.bot

    await bot.send_message(
        chat_id=303042807,
        text=(f"Ім'я:{name}\n"
              f"Телефон:{phone}\n"
              f"Пошта:{email}\n"
              f"Комментар:{comment}")
    )


ADMIN_ID = os.getenv("ADMIN_ID")
async def order(message:Message):

    user_id = message.from_user.id
    if user_id !=int(ADMIN_ID):
        await message.answer(    
            "В доступі відмовлено"
        )
    return   
        



@router.message(Command("orders"))
async def order(message: Message):
    tmp =message.text.split()
    if len(tmp) > 1:
        tmp1 = int(tmp[1])
        orders = database.get_orders(tmp1)
    else:
        orders = database.get_orders()
    

    for order in orders:
        await message.answer(
            f"ID:{order[0]}\n"
            f"Name:{order[1]}\n"
            f"Phone:{order[2]}\n"
            f"Email:{order[3]}\n"
            f"Comment:{order[4]}"

    )


@router.message(Command("delete"))
async def order(message:Message):
    mess = message.text
    temp = mess.split()
    order_id = int(temp[1])
    database.delete_order(order_id)

    await message.answer(
        f"Користувач із ID:{order_id} успішно видалений"
    ) 


@router.message(Command("update"))
async def order(message: Message):
    orders_update = message.text
    temp1 = orders_update.split()
    orders_update_id = int(temp1[1])
    new_comment = " ".join(temp1[2:])

    database.update_order(new_comment,orders_update_id)

    await message.answer(
        f"Користувач із ID:{orders_update_id} успішно оновив коментар на {new_comment}"
    )




    await state.clear()