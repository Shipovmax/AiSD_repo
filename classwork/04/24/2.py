from functools import reduce

find_anagrams_reduce = lambda target, words: reduce(
    lambda acc, word: acc + [word] if sorted(word) == sorted(target) else acc,
    words,
    []
)

print(find_anagrams_reduce('abcd', ['boda', 'abce', 'cbda', 'cbea', 'adcb']))



find_anagrams = lambda target, words: list(filter(lambda w: sorted(w) == sorted(target), words))

print(find_anagrams('abcd', ['boda', 'abce', 'cbda', 'cbea', 'adcb']))