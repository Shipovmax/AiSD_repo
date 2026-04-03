p = 0


def printin(s):
    global p
    print(p * "    " + s)
    p += 1


def printout(s):
    global p
    p -= 1
    print(f"{p * '    '}{s}")
    return s


def fib(n):
    printin(f"fib({n})")

    if n == 0:
        return printout(0)
    if n == 1:
        return printout(1)

    if n >= 2:
        return printout(fib(n - 1) + fib(n - 2))

    else:
        return printout(fib(n + 2) - fib(n + 1))


print("Результат:", fib(-6))
