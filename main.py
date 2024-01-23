import telebot,database as db,buttons as bt

bot = telebot.TeleBot("6399616653:AAEAc4mklFFJLryzQErOdcdODrcG0GeLvwY")
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Выбери одну из команд: /create /revise")
@bot.message_handler(commands=["create"])
def create(message):
    user_id = message.from_user.id
    if message.text.lower() == "/create":
        bot.send_message(user_id,"Введите слово:")
        bot.register_next_step_handler(message,src)

    else:
        bot.send_message(user_id,"Лох")
def src(message):
 wordb = message.text
 user_id = message.from_user.id
 bot.send_message(user_id, "Введите перевод:")
 bot.register_next_step_handler(message, sr,wordb)
def sr(message,wordb):
    translatee = message.text
    user_id = message.from_user.id
    bot.send_message(user_id, "Слово в словаре!\n Что делаем дальше?)",
                     reply_markup=bt.hh())
    db.register(wordb,translatee)
    if message.text.lower() == "/create":

        bot.register_next_step_handler(message, create)
    elif message.text.lower() == "/revise":

        bot.register_next_step_handler(message, revise)
@bot.message_handler(commands=["revise"])
def revise(message):
    user_id = message.from_user.id
    if message.text.lower() == "/revise":
      bot.send_message(user_id, "Перевод с немецкого или с русского:")
      bot.register_next_step_handler(message, spp)


def spp(message):
    user_id = message.from_user.id
    if message.text.lower() == "с немецкого" or message.text.lower() == "немецкий":
        b = db.ask_nem()
        bot.send_message(user_id,f'Введите слово из списка:{b}')
        bot.register_next_step_handler(message,nem)
    elif message.text.lower() == "с русского" or message.text.lower() == "русский":
        b = db.ask_ru()
        bot.send_message(user_id, f'Введите слово из списка:{b}')
        bot.register_next_step_handler(message, ru)
def nem(message):
    q = message.text
    user_id = message.from_user.id
    bot.send_message(user_id, "А теперь перевод!")
    bot.register_next_step_handler(message,ri,q)


def ri(message,q):
    user_id = message.from_user.id
    wordb = message.text
    b = db.ask_translate(wordb,q)
    bot.send_message(user_id, f'{b}\n'"Что делаем дальше?)", reply_markup=bt.hh())
    if message.text.lower() == "/create":
        bot.register_next_step_handler(message, create)
    else:

        bot.register_next_step_handler(message, revise)

def ru(message):
    q = message.text
    user_id = message.from_user.id
    bot.send_message(user_id,"А теперь перевод!")
    bot.register_next_step_handler(message,r,q)
def r(message,q):
    user_id = message.from_user.id
    wordb = message.text
    b = db.ask_translate_ru(wordb,q)
    bot.send_message(user_id, f'{b}\n'"Что делаем дальше?)",reply_markup=bt.hh())
    if message.text.lower() == "/create":

        bot.register_next_step_handler(message, create)
    else:

        bot.register_next_step_handler(message, revise)


bot.polling(non_stop=True)




