import telebot
from extensions import  obrabotka
from ssettings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message ):
    bot.send_message(message.chat.id, '''Добро пожаловать в CursBOT!💸
Бот создан для проверки актуального курса валют. При вводе команды /values можно увидеть доступные валюты.Для того чтобы узнать курс интересуемой валюты, сделайте следующий запрос:''')
    bot.send_message(message.chat.id, '<имя валюты, цену которой хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>')

@bot.message_handler(commands=['values'])
def handle_start_values(message: telebot.types.Message ):
    bot.reply_to(message, '''💰Доступные валюты:
     доллар 
     евро
     манат
     тенге
     юань
     рубль
     лира
''')

@bot.message_handler(content_types=['text'])
def handle_docs_audio(message):
    bot.reply_to(message, obrabotka(str(message.text)))

bot.polling(none_stop=True)