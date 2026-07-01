def issue(func):
    def wrapper(*args):
        rez = func(*args)
        if rez < 0:
            return -rez
        else:
            return rez

    return wrapper


@issue
def funk(a, b, c):
    return a + b + c


print(funk(3, -4, -5))
