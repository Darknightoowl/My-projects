import telebot ,random
from telebot import types
aaa = ['Нет ни лучшего, ни худшего пути. Есть только твой Путь.', 'Упади семь раз, но поднимись восемь', '«Сова - великий и довольно умный лесной старик. Он также может написать вторник ».', 'Руки матери успокаивают больше, чем чьи-либо еще».' '«Если вы не рискуете, вы не можете создать будущее!» ', '«Вы можете умереть в любое время, но жизнь требует настоящего мужества».', '«Бесполезно притворяться, что не видишь, что происходит».',  'Когда я учился в школе, у меня был только один репетитор — ремень ', 'Любовь котов к рыбе безответна.', 'А вы заметили в какое интересное время мы живем? И главное, что живем! ','А вы заметили в какое интересное время мы живем? И главное, что живем!', 'Хорошо жить, когда не надо больше, чем надо.', 'Мне сегодня сказали, что я офигенная! Или офигевшая... Блин, забыла.', 'Для того, чтобы начать меняться, нужно желание, а не понедельник' , 'Иногда умная мысль посещает голову. Но ее быстро вытесняет толпа тупы', 'Если проигравший улыбается, победитель теряет вкус победы.', 'Уничтожь, то что уничтожает тебя.' , 'Никто не идеален, кроме меня.']
bot= telebot.TeleBot('6126844099:AAF1aPImSF1_yMsBXQdzvwN6hk2yROaMNpw')

@bot.message_handler(commands=['start'])
def start(message):
   rf = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('шутки и цитаты',callback_data="quote")
   rf.add(btn1)
   
   bot.send_message(message.chat.id, random.choice(aaa),reply_markup=rf)
@bot.callback_query_handler(func = lambda call: True)
def all_calls(call):
    if call.data == "quote":
        rf = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('цитаты и шутки',callback_data="quote")
        rf.add(btn1)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = random.choice(aaa),reply_markup=rf)
bot.infinity_polling()