from PIL import Image, ImageFilter
import os
def z1():
    img = Image.open("тюльпан.jpg")
    img.show()
    print("Цветовая модель:", img.mode)
    print("Формат:", img.format)
    print("Размер:", img.size)

def z2():
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
    os.mkdir("pupu")
    for i in range(1,6):
        image = Image.open(f'{i}.jpg')
        img_smooth = image.filter(ImageFilter.DETAIL)
        img_smooth.save(f'filtereeee{i}.jpg')
def z4(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    watermark.putalpha(100)
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)


img = 'тюльпан.png'
z4(img, 'watermarka.png','1.jpg', position=(0, 0))


