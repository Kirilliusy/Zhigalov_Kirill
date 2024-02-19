color1=input("Введите название первого основного цвета с маленькой буквы: ")
color2=input("Введите название второго основного цвета с маленькой буквы: ")
if (color1 != 'жёлтый' and color1 != 'красный' and color1 != 'синий') or (color2 != 'жёлтый' and color2 != 'красный' and color2 != 'синий') or (color1==color2) :
    print("Введены не основные цвета или одинаковые")
else:
    if (color1=='жёлтый' and color2 == 'красный') or (color2=='жёлтый' and color1 == 'красный'):
        print("Получится оранжевый")
    elif (color1=='синий' and color2 == 'красный') or (color2=='синий' and color1 == 'красный'):
        print("Получится фиолетовый")
    elif (color1=='синий' and color2 == 'желтый') or (color2=='синий' and color1 == 'жёлтый'):
        print("Получится зелёный")