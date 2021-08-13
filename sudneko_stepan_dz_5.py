import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    """Функция возвращает шутки, в кол-ве введенного num"""
    joke_list = []
    for i in range(num):
        list_nouns = random.choice(nouns)
        list_adverbs = random.choice(adverbs)
        list_adjectives = random.choice(adjectives)
        joke_list.append(f'{list_nouns} {list_adverbs} {list_adjectives} ')
    return joke_list
print(get_jokes(4))