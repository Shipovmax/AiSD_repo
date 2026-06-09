"""
Дано предложение. С помощью `map`/`filter`/`reduce` удалите первую и последнюю буквы у каждого слова, и склейте в строку слова длиной > 5.
"""

from functools import reduce


def solve_task(sentence):

    words = sentence.split()
    trimmed_words = map(lambda w: w[1:-1], words)
    filtered_words = filter(lambda w: len(w) > 5, trimmed_words)

    result = reduce(lambda a, b: f"{a} {b}", filtered_words, "")

    return result.strip()
