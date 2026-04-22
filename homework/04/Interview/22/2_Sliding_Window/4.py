def length_of_longest_substring(s: str) -> int:
    '''
    Найди длину самой длинной подстроки без повторяющихся символов.
    '''

    char_set = set()
    left     = 0 
    max_len  = 0 

    for right in range(len(s)):
        # Убираем символы пока есть дубликаты 
        
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len,right - left + 1)

    return max_len

# Тест
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")

'''
Время  O(n)
Память O(n)
'''