# здесь прописаны функции для подачи всратых картинок и наших фото
# таких API нет, поэтому для открыток я сохранил url'ы. наши фото я сохранил в отдельную папку

import requests as r
import random

# 1 - всратые открытки
# нужно написать файл, в котором будут лежать url'ы
links = open('data/postcards_links.txt').read().splitlines()
compliments = open('data/chain_compliments.txt').read().splitlines()


def get_postcard():
    link = random.choice(links)

    # какие-то ссылки битые, поэтому обработаем падение
    try:
        if r.get(link).status_code == 200:
            return link
    except r.exceptions.MissingSchema:
        return 'Oops... Try again!'


# 2 - наши фотографии
# нужно собрать папку с нашими фото. пока сделаю папку с любыми фото и научу бота отправлять их
# def get_us():
#     number = random.choice(range(0, 74))
#     file_place = 'data/our_pics/picture' + str(number) + '.jpg'
#
#     return file_place


# 3 - нейрокомплименты

def get_neural_comp():
    compliment = random.choice(compliments)

    return compliment
