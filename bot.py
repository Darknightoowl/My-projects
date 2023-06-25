import telebot , random

bot = telebot.TeleBot('6126844099:AAF1aPImSF1_yMsBXQdzvwN6hk2yROaMNpw')

@bot.messege_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'hi')
     if message.text == 'привет' or message.text == 'как дела':
        bot.send_message(message.chat.id , random.choise(abc))

         else:

         bot.send_message(message.chat.id 'сова спит')

abc = ['привет', '(:', 'ты кто', 'добро пожаловать',]
      
      age = ['25' ,'18' , '15',]

      if message.text == 'сколько вам лет':
        bot.send_message(message.chat.id random.choise(age))

        else:
            bot.send_message(message.chat.id, 'сова спит')


 bot.infinity_poling(none_stop=true)
