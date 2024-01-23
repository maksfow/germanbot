from telebot import types

def hh():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    rr = types.KeyboardButton("/create")
    rk = types.KeyboardButton("/revise")
    # Добавляем кнопки в пространство
    kb.add(rr,rk)
    return kb