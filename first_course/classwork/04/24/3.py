a = ['adda', 'abcba','asdqc', '67']
rez = list(filter(lambda x: x == x[::-1], a))
print(rez)

