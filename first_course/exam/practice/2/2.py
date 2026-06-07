'''
Декоратор, который проверяет предусловие перед выполнением функции.
'''

from typing import Type, Optional, Callable, Any
from functools import wraps


def validate_preconditions(validator: Callable[[Any], bool], error_msg: str):

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Проверяем первый аргумент (обычно это основной входной параметр)
            if not validator(args[0] if args else None):
                raise Va