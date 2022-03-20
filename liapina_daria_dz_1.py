def num_translate():
    num = input('Введите число на английском от 0 до 10: ')
    print(translate_dict.get(num))
translate_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'for': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
num_translate()