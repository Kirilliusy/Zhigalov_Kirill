place = int(input("Введите номера места"))
numb=""
if place >0 and place <55:
    if place % 2 == 0 :
        if place < 55 and place > 36:
            numb="Верхнее боковое"
        else:
            numb = "Верхнее купе"
    else:
        if place < 55 and place > 36:
            numb="Нижнее боковое"
        else:
            numb = "Нижнее купе"
else:
    print("Такого места нет")
    exit()
print(f"Ваше место {numb}")