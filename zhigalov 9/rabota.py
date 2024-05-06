import os
import csv
from pathlib import Path
from PIL import Image, ImageFilter
import shutil
def z1():
    os.mkdir("papa")
    for i in os.listdir():
        if Path(i).suffix == ".jpg":
            image = Image.open(i)
            img_smooth = image.filter(ImageFilter.DETAIL)
            img_smooth.save(f'filtereeee({i}).jpg')
            f = open(os.path.join("papa", f'filtereeee({i}).jpg'), 'a')
            os.remove(f'filtereeee({i}).jpg')
        else:
            f = open(os.path.join("papa", i), 'a')
            os.remove(i)
def z3():
    print("Нужно купить:")
    with open('zad.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            name, col, price = "".join(row).split(";")
            print(f"{name} - {col} шт. за {price} руб.")

z3()
