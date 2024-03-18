def happy():
    a = str(input("Введите номер билета: "))
    if len(a) % 2 == 0:
        leng = int(len(a)/2)
        b = a[leng:]
        c = a[:leng]
        if sum(map(int, b)) == sum(map(int, c)):
            print("Ура, у вас счастливый билет!")
        else:
            print("Увы, ваш билет не счастливый")
    else:
        print("Длина введёного числа должна быть чётной")
happy()
