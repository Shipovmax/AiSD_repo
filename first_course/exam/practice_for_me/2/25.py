"""
Создайте параметризованный декоратор tol(dlina, fill).

Он должен трансформировать результат работы декорируемой функции в словарь,
состоящий строго из dlina элементов.

Если функция возвращает меньше элементов, декоратор заполняет недостающие позиции значением fill.

Если функция возвращает больше элементов — декоратор жестко "обрезает хвост" до заданной длины.

"""


def tol(dlina, fill):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, dict):
                items = list(result.items())
            else:
                try:
                    items = list(result)
                except TypeError:
                    items = [result]

            if len(items) < dlina:
                for i in range(len(items), dlina):
                    items.append((f"auto_key_{i}", fill))
            elif len(items) > dlina:
                items = items[:dlina]

            return dict(items[:dlina])

        return wrapper

    return decorator


@tol(dlina=3, fill="empty")
def get_short_dict():
    return {1: "a"}


@tol(dlina=3, fill="empty")
def get_long_list():
    return [("x", 10), ("y", 20), ("z", 30), ("w", 40)]
