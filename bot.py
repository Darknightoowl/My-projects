import telebot ,random
from telebot import types




aaa = ['Нет ни лучшего, ни худшего пути. Есть только твой Путь.', 'Упади семь раз, но поднимись восемь', '«Сова - великий и довольно умный лесной старик. Он также может написать вторник ».', 'Руки матери успокаивают больше, чем чьи-либо еще».']
bot= telebot.TeleBot('6126844099:AAF1aPImSF1_yMsBXQdzvwN6hk2yROaMNpw')

@bot.message_handler(commands=['start'])

def start(message):
   rf = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('цитата',callback_data="quote")
   rf.add(btn1)
   bot.send_message(message.chat.id, random.choice(aaa),reply_markup=rf)
@bot.callback_query_handler(func = lambda call: True)
def all_calls(call):
    if call.data == "quote":
        rf = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('цитата',callback_data="quote")
        rf.add(btn1)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = random.choice(aaa),reply_markup=rf)
bot.infinity_polling()