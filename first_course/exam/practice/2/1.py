from typing import Type, Optional, Callable, Any
from functools import wraps

class AiSDError(Exception):
    pass

class ValidationError(AiSDError):
    """Вызывается, когда входные данные не соответствуют заданным ограничениям."""
    pass

class AlgorithmConvergenceError(AiSDError):
    """Вызывается, когда итерационный алгоритм не сошелся за заданное количество шагов."""
    pass

class OutOfBoundsError(AiSDError):
    """Вызывается при попытке доступа к элементу за пределами границ структуры данных."""
    pass


'''
Декоратор, который проверяет предусловие перед выполнением функции.
'''

def validate_preconditions(validator: Callable[[Any], bool], error_msg: str):

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Проверяем первый аргумент (обычно это основной входной параметр)
            if not validator(args[0] if args else None):
                raise ValidationError(f'Нарушен контракт: {error_msg}')
            return func(*args,**kwargs)
        return wrapper
    return decorator

