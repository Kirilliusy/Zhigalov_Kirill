def magic():
    a = input("Введите дату: ")
    b = a.split('.')
    if int(b[1])*int(b[0]) == int(b[2])%100:
        print("Ваша дата магическая")
    else:
        print("К сожалению ваша дата не магическая((")
magic()
