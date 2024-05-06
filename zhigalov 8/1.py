from PIL import Image, ImageDraw, ImageFont
import os


def z1():
    img = Image.open('Открытка.jpg')
    print(img.size)
    img_cropped = img.crop((50,50,500,450))
    img_cropped.save('обрезка.jpg')
    img_cropped.show()

def z2():
    directory = "праздники/"
    postcards = {"др": "др.jpg",
                 "1 сентября": "1сентября.jpg",
                 "1 мая": "1мая.jpeg",
                 "вербное воскресенье": "верба.jpg"}

    counter = 0
    for key in postcards.keys():
        print(f'{counter}) {key}')
        counter += 1

    holiday = input("Введите название праздника для получения открытки\n")

    if holiday in postcards:
        img = Image.open(directory + postcards.get(holiday))
        img.show()
    else:
        print('Такого праздника в словаре нет')
