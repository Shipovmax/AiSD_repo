def double(string: str) -> str:
    if not string:
        return ""
    return string[0] * 2 + double(string[1:])