def task1():
    country = {'Россия': 'Москва', 'Украина': 'Киев','Беларусь':'Минск','Эстония':'Таллин', "Германия": "Берлин", "Италия": "Рим" }
    ctr = input("Введите название страны: ")
    stl = country.get(ctr)
    print(stl)
    print(country.items())
    print(sorted(country.items()))
#task1()
def task2():
    erud = {
        1: ['А','В','Е','И','Н','О','Р','С','Т'],
        2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
        3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        4: ['Й', 'Ы'],
        5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        8: ['Ш', 'Э', 'Ю'],
        10: ['Ф', 'Щ', 'Ъ']}
    kol = 0
    word = input("Введите своё слово: ").upper()
    wordn = list(word)
    for i in range(len(wordn)):
        kol += erud.get(wordn[i])
    print()
task2()