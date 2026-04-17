def double(string: str) -> str:
    if not string:
        return ""
    return string[0] * 2 + double(string[1:])

print(double("abc"))   # "aabbcc"
print(double("hello")) # "hheelllloo"
print(double(""))      # ""