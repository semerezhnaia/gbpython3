from random import choice

def get_jokes(x):
    list_jokes = []
    for i in range(x):
        joke = ' '.join([choice(nouns), choice(adverbs),choice(adjectives)])
        list_jokes.append(joke)
    print(list_jokes)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(3)