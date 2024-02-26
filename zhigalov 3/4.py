import random
def MathForKids():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int(input(f'{a} + {b} = '))
    return (a + b) == c
k = 0
t = 0
while k < 3:
    if not(MathForKids()):
        k += 1
    else:
        t += 1
print("Игра Окончена. Правильных ответов: ", t)





