from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.telebot('5935816764:AAG7num21_q46K_F3JuDSeyF-Ka83yLTtIU')

@bot.message_handler(commands = ['start']) # Обработчик команд
def start(message):
    marcup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')

    marcup.add(itembtn1, itembtn2)
    bot.send_message(chat_id=message.chat.id, text="<b>Конвектер Валют</b>", reply_marcup=marcup, parse_mode="html")

    
@bot.message_handler(content_typse=['text']) # Обработчик контент 
def message(message):
    message_norm = message.text.strip().lower()
    if message_norm in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now()) # Ставка курс на данный момент.
        bot.send_message(chat_id=message.chat.id, text=f"<b>{message_norm.upper()} rate is {float(rates[message_norm.upper()])}</b>", parse_mode="html")

bot.polling(none_stop=True)