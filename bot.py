import telebot ,random
from telebot import types
aaa = ['Нет ни лучшего, ни худшего пути. Есть только твой Путь.', 'Упади семь раз, но поднимись восемь', '«Сова - великий и довольно умный лесной старик. Он также может написать вторник ».', 'Руки матери успокаивают больше, чем чьи-либо еще».' '«Если вы не рискуете, вы не можете создать будущее!» ', '«Вы можете умереть в любое время, но жизнь требует настоящего мужества».', 'Никто не ценит того, чего слишком много.', 'Все что нам нужно — это любовь.', 'Никто не идеален, кроме меня.', 'Я помню все, что я забыла…', 'если жизнь не дарует то на то что мы надеемся подленный дар это сама жтзнь', 'у тебя всегда будет способ проникать в сердца людей', 'меня всегда будут преследовать мои действия', 'Счастье — это образ мышления.', 'Без боли кто бы знал, что такое наслаждение?', 'Всё начинается с осознания собственных слабостей.', 'Человек взрослеет, побеждая над своим жалким прошлым.', 'Но, как говорится, ни одно доброе дело не остается безнаказанным.']
bot= telebot.TeleBot('6126844099:AAF1aPImSF1_yMsBXQdzvwN6hk2yROaMNpw')
joke = ['Хороший собеседник не только слушает, но и подливает.', 'Если план А не сработал, не сдавайся — у тебя есть ещё 32 буквы, чтобы попробовать', 'Эх. Сейчас бы собрать все деньги, которые я когда-то пропил… И снова их пропить…', 'Ничто так не ориентирует человека на местности, как поиски ', 'Через гены детям передаются не только болезни, но и деньг', 'Единственный реально действующий тест на корону - надо вытащить меч из камня...', 'Совы часто поворачивают голову на сто восемьдесят градусов, и только один раз в жизни — на 360', 'Вчера был на вечеринке у совы. Все было прям ух.', 'Совы — очень мудрые птицы. Вы где-нибудь видели сову оформляющую кредит? То-то же.', 'Летит пьяный филин по лесу ночью: — Угу. Угу. Угу. (Бом!) Ого!.', 'В жизни, как в компьютерной игре: чем лучше сохранился - тем лучше жив', 'Обучаю игре в преферанс - плачу стипендию в размере половины проигрыша.']
@bot.message_handler(commands=['start'])
def start(message):
   rf = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Цитаты',callback_data="quote")
   btn2 = types.InlineKeyboardButton("Шутки", callback_data="joke")
   rf.add(btn1,btn2)
   bot.send_message(message.chat.id, "Выберите Цитаты или Шутки",reply_markup=rf)

@bot.callback_query_handler(func = lambda call: True)
def all_calls(call):
    if call.data == "quote":
        rf = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Рандомные Цитаты',callback_data="quote")
        rf.add(btn1)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = random.choice(aaa),reply_markup=rf)
    elif call.data == "joke":
        owl = types.InlineKeyboardMarkup()
        vb2 = types.InlineKeyboardButton('Рандомные Шутки', callback_data = 'joke')
        owl.add(vb2)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = random.choice(joke),reply_markup=owl)

bot.infinity_polling()