import requests
from bs4 import BeautifulSoup
from ssettings import currencies

class MessageException(Exception):
    def __str__(self):
        return "😡Неправильный запрос. Повторите попытку."

class SameCurrenciesException(Exception):
    def __str__(self):
        return "😡Неправильный запрос: Вы ввели две одинаковые валюты. Повторите попытку."

class VrongAmountException(Exception):
    def __str__(self):
        return "😡Неправильный запрос: Вы некорректно ввели количество первой валюты. Повторите попытку."

class VrongFirstCurrencyException(Exception):
    def __str__(self):
        return "😡Неправильный запрос: Название первой валюты введено некорректно либо вы ввели недоступную валюту. Названия доступных валют /values. Повторите попытку."

class VrongSecondCurrencyException(Exception):
    def __str__(self):
        return "😡Неправильный запрос: Название второй валюты введено некорректно либо вы ввели недоступную валюту. Названия доступных валют /values. Повторите попытку."

class Zapros:
    def __init__(self, base, quote, amount, currencies):
        self.base = base
        self.quote = quote
        self.amount =amount
        self.currencies = currencies
    def get_price(self):
        html = requests.get('https://www.banki.ru/products/currency/cb/').content
        soup = BeautifulSoup(html, 'lxml')
        tbody = soup.find('tbody')
        a = tbody.find_all('tr')
        if self.quote == 'рубль' or self.quote == 'Рубль':
            val1 = a[self.currencies[self.base]].getText().split()
            valut1 = (float(val1[-2]) / float(val1[1]))*self.amount
            return valut1
        elif self.base == 'рубль' or self.base == 'Рубль':
            val2 = a[self.currencies[self.quote]].getText().split()
            valut2 = (1/(float(val2[-2]) / float(val2[1])))*self.amount
            return valut2
        else:
            val1 = a[self.currencies[self.base]].getText().split()
            valut1 = (float(val1[-2]) / float(val1[1]))
            val2 = a[self.currencies[self.quote]].getText().split()
            valut2 = (float(val2[-2]) / float(val2[1]))
            return ((valut1 * self.amount)/valut2)

def obrabotka(users_message: str):
    a = users_message.split()
    try:
        if len(a) == 3:
            pass
        else:
            raise MessageException
        if a[1] != a[0]:
            pass
        else:
            raise SameCurrenciesException
        if a[0] in currencies:
            pass
        else:
            raise VrongFirstCurrencyException
        if a[1] in currencies:
            pass
        else:
            raise VrongSecondCurrencyException
        try:
            float(a[2])
            pass
        except ValueError:
            raise VrongAmountException
    except BaseException as e:
        return e
    else:
        a[2] = float(a[2])
        soob = Zapros(a[0], a[1], a[2], currencies)
        return soob.get_price()

