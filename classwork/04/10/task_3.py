def issue(func):
    def wrapper(*args, **kwargs):
        name, old = func(*args, **kwargs)

        name = name[::-1]
        old = int(str(old)[::-1])

        return name, old

    return wrapper


@issue
def funk(name, old):
    return name, old


print(funk("qwe", 12))
