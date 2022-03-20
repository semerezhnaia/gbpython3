def thesaurus(*args):
    name_dict= {}
    for name in args:
        first_letter = name[0]
        name_dict[first_letter] = name_dict.get(first_letter, []) + [name]
    return name_dict

print(thesaurus('Кирилл', 'Алена', 'Максим', 'Вероника', 'Юлия', 'Наталья', 'Настасья'))
