# здесь я прописал логику взаимодействия с некоторыми API для бота
import requests as r


# 1 - собачки
def get_doggy():
    dogs_link = 'https://random.dog/woof.json'
    try:
        dogs_url = r.get(dogs_link).json()['url']
        return dogs_url
    except:
        return "Ooops... Try again)"


# 2 - лисички
def get_foxy():
    foxes_link = 'https://randomfox.ca/floof/'
    try:
        foxy_url = r.get(foxes_link).json()['image']
        return foxy_url
    except:
        return "Ooops... Try again)"


# 3 - кошечки
def get_kitty():
    cats_link = 'https://aws.random.cat/meow'
    try:
        kitty_url = r.get(cats_link).json()['file']
        return kitty_url
    except:
        return "Ooops... Try again)"


# 4 - шутки от бати
def get_dady_joke():
    jokes_link = 'https://icanhazdadjoke.com/slack'
    try:
        joke = r.get(jokes_link).json()['attachments'][0]['fallback']
        return joke
    except:
        return "Ooops... Try again)"


# 5 - факты про числа
def get_fact_about_number(number):
    digits_link = 'http://numbersapi.com/'
    try:
        fact = r.get(digits_link + str(number)).text
        return fact
    except:
        return "Ooops... Try again)"


# 6 - шутки про Чака Норисса
def get_chuck_joke():
    chuck_jokes_link = 'https://api.chucknorris.io/jokes/random'
    try:
        joke = r.get(chuck_jokes_link).json()['value']
        return joke
    except:
        return "Ooops... Try again)"
