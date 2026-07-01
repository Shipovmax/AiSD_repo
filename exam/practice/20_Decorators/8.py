'''
Создайте декоратор decor(a). Приводит в верхний регистр значения словаря, чьи ключи кратны a.
'''


def decor(a: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result_dict = func(*args, **kwargs)

            if not isinstance(result_dict, dict):
                return result_dict

            new_dict = {}
            for key, value in result_dict.items():
                if isinstance(key, (int, float)) and key % a == 0:
                    if isinstance(value, str):
                        new_dict[key] = value.upper()
                    else:
                        new_dict[key] = value
                else:
                    new_dict[key] = value

            return new_dict

        return wrapper

    return decorator


@decor(a=3)
def get_data():
    return {
        1: "apple",
        3: "banana",
        5: "cherry",
        6: "date",
        9: 123
    }


print(get_data())
