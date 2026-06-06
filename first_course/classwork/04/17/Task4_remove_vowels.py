VOWELS = set("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ")


def remove_vowels(string: str) -> str:
    if not string:
        return ""
    head, *tail = string
    return (head if head not in VOWELS else "") + remove_vowels("".join(tail))
