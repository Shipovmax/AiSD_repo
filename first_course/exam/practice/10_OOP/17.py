'''
Реализуйте класс-калькулятор, выполняющий арифметические операции (+ и -).
Программа принимает строку вида 6 - 7 + 4.
'''


class Calculator:
    def __init__(self, expression: str):
        self.expression = expression

    def calculate(self) -> int:
        tokens = self.expression.split()
        if not tokens:
            return 0

        result = int(tokens[0])
        i = 1

        while i < len(tokens):
            operator = tokens[i]
            next_value = int(tokens[i + 1])

            if operator == "+":
                result += next_value
            elif operator == "-":
                result -= next_value

            i += 2

        return result


calc = Calculator("6 - 7 + 4")
print(f"Результат выражения: {calc.calculate()}")
