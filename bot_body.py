import telebot
from DB_actions import get_postcard, get_neural_comp
from API_actions import get_foxy, get_doggy, get_kitty, get_dady_joke, get_chuck_joke, get_fact_about_number
from answer import bot_answer
from config import my_token, annotation, my_functions

bot = telebot.TeleBot(my_token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_photo(message.chat.id, open('data/start.jpg', 'rb'), caption=annotation)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, my_functions)


@bot.message_handler(commands=["fox"])
def fox(message):
    content = get_foxy()
    bot.send_message(message.chat.id, content)


@bot.message_handler(commands=["dog"])
def dog(message):
    content = get_doggy()
    bot.send_message(message.chat.id, content)


@bot.message_handler(commands=["cat"])
def cat(message):
    content = get_kitty()
    bot.send_message(message.chat.id, content)


def check_text(text):
    values = text.split()
    if len(values) != 2:
        return False, 'Enter in "/fact number" format please'

    try:
        return True, int(values[1])
    except ValueError:
        return False, 'Enter in "/fact number" format please'


@bot.message_handler(commands=["fact"])
def fact(message):
    text = message.text
    success, value = check_text(text)
    if success:
        content = get_fact_about_number(value)
        bot.send_message(message.chat.id, content)
    else:
        bot.send_message(message.chat.id, value)


@bot.message_handler(commands=["joke"])
def joke(message):
    content = get_dady_joke()
    bot.send_message(message.chat.id, content)


@bot.message_handler(commands=["chuck"])
def chuck(message):
    content = get_chuck_joke()
    bot.send_message(message.chat.id, content)


@bot.message_handler(commands=["card"])
def card(message):
    content = get_postcard()
    bot.send_message(message.chat.id,
                     "If a postcard didn't appear, try again or follow the link")
    bot.send_message(message.chat.id, content)


@bot.message_handler(commands=["setmain"])
def setmain(message):
    bot.send_message(message.chat.id, "Yes, Milady?")


@bot.message_handler(commands=["we"])
def we(message):
    try:
        file = get_us()
        bot.send_photo(message.chat.id, open(file, 'rb'), "Чмок")
    except:
        bot.send_message(message.chat.id, "Ooops... Try again)")



@bot.message_handler(commands=["neuro"])
def neural(message):
    compliment = get_neural_comp()
    bot.send_message(message.chat.id, compliment)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    answer_text = bot_answer(message)
    bot.reply_to(message, answer_text)


bot.polling()
