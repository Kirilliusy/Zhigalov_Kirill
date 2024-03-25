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
