def task1():
    numb = [3,6,9,24,34]
    numuser = int(input("Введите ваше число: "))
    if numuser in numb:
        print('Вот исходный список - ', numb)
        print("Ваше число есть в списке!")
    else:
        print('Вот исходный список - ', numb)
        print('Вы не угадали число((')
task1()

import random
def task2():
    rndm = [""]*10
    for i in range(0,10):
        rndm[i] = random.randrange(1,100)
    print(rndm)
    k=0
    for i in range(0,9):
        for j in range(i+1,9):
            if rndm[i] == rndm[j]:
                k+=1
    if k>0:
        print(f"Повторяющихся элементов - {k}")
    else:
        print('Нет повторяющихся элементов')
task2()

def task3():
    days = ('Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье')
    hday = int(input("Введите количество желаемых выходных: "))
    print('Ваши выходные дни: ', days[7-hday:7])
    print('Ваши рабочие дни: ', days[0:7-hday])
task3()

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
