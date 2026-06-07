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