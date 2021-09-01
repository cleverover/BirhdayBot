import json

def load_config():
    with open('data/BOT_CONFIG.json', 'rb') as f:
        BOT_CONFIG = json.load(f)
    return BOT_CONFIG

check_list = list(range(97, 123)) + list(range(65, 91)) + list(range(1072, 1104)) + list(range(1040, 1072))

my_token = 'Iwillnotpostitihere'

annotation = '''Hi, bro!
Lesha specially made me for your birthday.
He decided, that my advantage is absence of physical existing.
You won't have to service me, find place for me or recycle me.
Just write to me and lift up your mood)

I can send:
1. Nice foxes - /fox
2. Nice cats - /cat
3. Nice dogs - /dog
4. Funny postcards - /card
5. Funny jokes - /joke
6. Chuck Norris jokes - /chuck
7. An interesting fact about number - /fact number
8. A neural compliment - /neuro
9. You know - /setmain

Unfortunately, I know people's language not very well, but you cat try to text with me!
By the way, I speak only russian(

You may write /help next time and I'll remind my functions to you.'''

my_functions = '''
1. Nice foxes - /fox
2. Nice cats - /cat
3. Nice dogs - /dog
4. Funny postcards - /card
5. Funny jokes - /joke
6. Chuck Norris jokes - /chuck
7. A fact about number - /fact number
8. A neural compliment - /neuro
9. You know - /setmain
'''
