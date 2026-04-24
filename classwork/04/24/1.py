a = 4

# Большое решение

def func(x: int) -> int :
    return x**3
rez = func(a)
print(rez)

# Короткое решение

rez = lambda x:x**3
print(rez)

# ---------------------------------

b = [4,2,3,6,7]

rez = list(map(lambda x:x**3,b))
print(rez)

# ---------------------------------

a =['aw', 'dfg', 'acpo']

rez = list(filter(lambda x:x.upper() if x[0]=='a' else 0 , a))
print(rez)


# ---------------------------------

a = [1, 2, 3, 4, 5, 6]

rez = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))
print(rez)  # [4, 16, 36]
