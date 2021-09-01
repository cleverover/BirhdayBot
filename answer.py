import nltk
import random
from config import load_config, check_list

BOT_CONFIG = load_config()


def clean(text):
    output_text = ''
    for let in text:
        if ord(let) in check_list or let == "'":
            output_text += let
    return output_text


def get_intent(text):
    text = text.text
    try:
        for intent in BOT_CONFIG['intents'].keys():
            for example in BOT_CONFIG['intents'][intent]['examples']:
                text1 = clean(example)
                text2 = clean(text)
                if len(text1) * len(text2) != 0:
                    if nltk.edit_distance(text1, text2) / max(len(text1), len(text2)) < 0.6:
                        return intent

    except KeyError:
        return 'fail'

    return 'fail'


def bot_answer(text):
    intent = get_intent(text)
    if intent == 'fail':
        return f'Кожаный мешок сказал "{text}",\nно я ничего не понялб.'

    return random.choice(BOT_CONFIG['intents'][intent]['examples'])
