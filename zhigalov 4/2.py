def del100():
    try:
        a = int(input("Введите число на которое будем делить: "))
        print(f'Ваш результат - {100 / a}')
    except:
        print("Введён ноль или строка")
del100()
