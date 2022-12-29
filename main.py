import telebot
from extensions import MessageException1, MessageException2, MessageException3, MessageException4, MessageException5, Zapros

TOKEN = "МЕСТО ДЛЯ ТОКЕНА"
bot = telebot.TeleBot(TOKEN)

currencies = {'доллар': 0,
              'евро': 1,
              'манат': 3,
              'тенге': 13,
              'юань': 16,
              'рубль': None,
              'лира': 25,
              'Доллар': 0,
              'Евро': 1,
              'Манат': 3,
              'Тенге': 13,
              'Юань': 16,
              'Рубль': None,
              'Лира': 25
             }

def obrabotka(users_message: str):
    a = users_message.split()
    try:
        if len(a) == 3:
            pass
        else:
            raise MessageException1
        if a[1] != a[0]:
            pass
        else:
            raise MessageException2
        if a[0] in currencies:
            pass
        else:
            raise MessageException4
        if a[1] in currencies:
            pass
        else:
            raise MessageException5
        try:
            float(a[2])
            pass
        except ValueError:
            raise MessageException3
    except BaseException as e:
        return e
    else:
        a[2] = float(a[2])
        soob = Zapros(a[0], a[1], a[2], currencies)
        return soob.get_price()

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message ):
    bot.send_message(message.chat.id, '''Добро пожаловать в CursBOT!💸
Бот создан для проверки актуального курса валют. При вводе команды /values можно увидеть доступные валюты.Для того чтобы узнать курс интересуемой валюты, сделайте следующий запрос:''')
    bot.send_message(message.chat.id, '<имя валюты, цену которой хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>')

@bot.message_handler(commands=['values'])
def handle_start_values(message: telebot.types.Message ):
    bot.send_message(message.chat.id, '''💰Доступные валюты:
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
    bot.send_message(message.chat.id, obrabotka(str(message.text)))

bot.polling(none_stop=True)