from operator import itemgetter

class Lib:
    """ Библиотека """

    def __init__(self, id, name, memory, lang_id):
        self.id = id
        self.name = name
        self.memory = memory
        self.lang_id = lang_id

class Lang:
    """ Язык программирования"""
    def __init__(self, id, title):
        self.id = id
        self.title = title

class LibLang:
    """ Библиотеки языков программирования для реализации связи многие-ко-многим"""
    def __init__(self, lang_id, lib_id):
        self.lib_id = lib_id
        self.lang_id = lang_id

# Языки программирования
langs = [
    Lang(1, 'Python'),
    Lang(2, 'JavaScript'),
    Lang(3, 'Java'),
    Lang(5, 'C++'),
    Lang(6, 'C#'),
    Lang(7, 'Delphi')
]
# библиотеки
libs = [
    Lib(1, 'Pandas', 890, 1),
    Lib(2, 'Matplotlib', 950, 2),
    Lib(6, 'Voca', 754, 2),
    Lib(3, 'Maven', 489, 3),
    Lib(4, 'Leaflet', 481, 5),
    Lib(5, 'SFML', 678, 6),

    Lib(7, 'VCL',350 , 6)
]

libs_langs = [
    LibLang(1,1),
    LibLang(2,2),
    LibLang(2,6),
    LibLang(3,3),
    LibLang(5,4),
    LibLang(6,5),
    LibLang(6,7),
    LibLang(7,1),
    LibLang(7,2),
    LibLang(7, 3),
    LibLang(7, 4)

]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(l.name, l.memory, la.title)
                    for la in langs
                    for l in libs
                    if l.lang_id == la.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(la.title, lal.lang_id, lal.lib_id)
                         for la in langs
                         for lal in libs_langs
                         if la.id == lal.lang_id]

    many_to_many = [(l.name, l.memory, lang_title)
                    for lang_title, lang_id, lib_id in many_to_many_temp
                    for l in libs if l.id == lib_id]

    print('Задание B1')
    res_11 = []
    for i in one_to_many:
        if i[0][0] == "M":
            res_11.append([i[0],i[2]])
    print(res_11)

    print('\nЗадание B2')
    res_22 = []
    res_22 = [[one_to_many[0][2], one_to_many[0][1]]]
    for name, memory, title in one_to_many:
        if title == res_22[len(res_22) - 1][0]:
            if memory < res_22[len(res_22) - 1][1]:
                res_22[len(res_22) - 1][1] = memory
        else:
            res_22.append([title, memory])
    print(sorted(res_22, key=itemgetter(1)))

    print('\nЗадание B3')
    res_33 = []
    for title,memory, lib in many_to_many:
        res_33.append([title, lib])
    print(sorted(res_33, key=itemgetter(0)))



if __name__ == "__main__":
    main()
