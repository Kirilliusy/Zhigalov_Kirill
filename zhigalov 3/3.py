c = ""
while c != 'stop':
    c = input('Введите новое слово: ')
    if c != 'stop':
        if 'ф' in c or 'Ф' in c:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')

