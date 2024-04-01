import random
def task2():
    rndm = [""]*10
    for i in range(0,10):
        rndm[i] = random.randrange(1,100)
    print(rndm)
    k=0
    for i in range(0,9):
        for j in range(i+1,9):
            if rndm[i] == rndm[j]:
                k+=1
    if k>0:
        print(f"Повторяющихся элементов - {k}")
    else:
        print('Нет повторяющихся элементов')
task2()