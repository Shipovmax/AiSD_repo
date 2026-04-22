def reverse_string(s: list[str]) -> None :
    '''
    Разверни строку (массив символов) на месте.
    '''
    
    left = 0 
    right = len(s) - 1

    while left < right :
        s[left], s[right] = s[right], s[left]
        left  += 1
        right -= 1

# Тест 

s = ['h','e','l','l','o']
print(s)
reverse_string(s)
print(s)

'''
Время  O(n)
Память O(1)
'''