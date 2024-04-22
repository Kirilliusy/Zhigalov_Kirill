def z1():
    from PIL import Image
    img = Image.open("тюльпан.jpg")
    img.show()
    print("Цветовая модель:", img.mode)
    print("Формат:", img.format)
    print("Размер:", img.size)

def z2():
    from PIL import Image
    img = Image.open("тюльпан.jpg")
    small = img.reduce(3)
    small.save("меньше_тюльпан.jpg")
    horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    horizontal.save("горизонт.jpg")
    vertical.save("вертикал.jpg")
    img.show()
    horizontal.show()
    vertical.show()
    small.show()
def z3():
    from PIL import Image, ImageFilter
    import os
    os.mkdir("е")
    for i in range(1,6):
        image = Image.open(f'{i}.jpg')
        img_smooth = image.filter(ImageFilter.SMOOTH)
        img_smooth.save(f'е/фильтр{i}.jpg')
