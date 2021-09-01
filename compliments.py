# цель - обучить алгоритм генерировать комплименты (на марковских цепях, например)
# задача - набрать базу данных с комплиментами (пока на английском)

import requests as r

def add_compliment():
    link = 'https://complimentr.com/api'
    text = r.get(link).json()['compliment']

    with open('compliments_eng.txt', 'a') as f:
        f.write(text)
        f.write('\n')

    return 0

counter = 0
epoch = 1000

for i in range(epoch):
    add_compliment()
    counter += 1

    if counter % 100 == 0:
        print(f"Saved: {counter} compliments")
