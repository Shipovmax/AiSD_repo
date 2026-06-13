"""
Реализуйте параметризованный декоратор decor(a).

Он должен применять изменения к возвращаемому функцией словарю:
все строковые значения, чьи ключи являются числовыми и кратны параметру a,
должны быть приведены к верхнему регистру (UPPERCASE).
"""


def decor(a):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, dict):
                return result

            for key, value in result.items():
                if isinstance(key, (int, float)) and key % a == 0:
                    if isinstance(value, str):
                        result[key] = value.upper()
            return result

        return wrapper

    return decorator


@decor(a=3)
def get_data():
    return {3: "hello", 6: "world", 5: "apple", 9: 123, "3": "text"}
