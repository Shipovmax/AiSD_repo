def summa(a, b):
    '''Функция, которая возвращает сумму двух чисел'''
    return a + b


def raznost(a, b):
    '''Функция, которая возвращает разность двух чисел'''
    return a - b


def hello(a,b):
    '''Функция, которая возвращает строку "Hi, " + имя'''
    return 'Hi, ' + a + ' ' + b

def main(*k):
    d = dict()
    for i in k:
        d[i.__doc__.split()[0]] = i
    return d
main('summa', 'raznost', 'hello')

new = main(summa, raznost , hello)
print(new)
for i,j in new.items():
    print(j(2,3))