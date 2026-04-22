'''
Даны две строки. Определи, являются ли они анаграммами.
'''


# Вариант когда можно юзать библиотеки

from collections import Counter

def is_anagram(s:str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Вариант когда нельзя юзать библиотеки

def is_anagram_v2(s:str, t: str) -> bool:
    
    # Проверка на сходство длин строк 
    if len(s) != len(t):
        return False
    
    count = {}
    
    for c in s:
        count[c] = count.get(c,0) + 1 # Если встретили то добавляем счетчик
    for c in t:
        count[c] = count.get(c, 0) - 1 # Если встретили то убавляем счетчик

    return all(v == 0 for v in count.values())

# Тест
print(is_anagram("anagram", "nagaram"))   # True
print(is_anagram("rat", "car"))           # False