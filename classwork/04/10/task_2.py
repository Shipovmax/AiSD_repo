def issue(func):
    def wrapper(*args):
        rez = func(*args) * 3
        return rez

    return wrapper


@issue
def funk(name):
    return name


print(funk("qwe"))
