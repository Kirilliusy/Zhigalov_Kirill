import random


def task4():
    MyGr = ["Жигалов", "Удовкин", "Павлова", "Агеечкина", "Розина", "Федорчук", "Игнатенко", "Пичуева", "Коченков", "Ридер"]
    DrGr = ["Иванов", "Петров", "Сидоров", "Смирнов", "Даут", "Ходырев", "Зайцев", "Шишикин", "Камаев", "Голев"]
    print(MyGr)
    print(DrGr)
    team = ['']*10
    for i in range(0,5):
        team[i] = MyGr[i]
    for i in range(5, 10):
        team[i] = DrGr[i]
    korteam = sorted(tuple(team))
    print("Ваша команда - ", korteam)
    print(f"Количество игроков - {len(korteam)}")
    k = 0
    if "Иванов" in korteam:
        for i in range(0,10):
            if "Иванов" == korteam[i]:
                k+=1
        print(f'Иванов встречается - {k} раз')
    else:
        print("Иванов не встречается")
task4()