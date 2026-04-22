"""
Вычисли значение выражения в обратной польской нотации.
Пример: ["2","1","+","3","*"] = (2+1)*3 = 9
"""


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {"+", "-", "*", "/"}

    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop() 
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
        else:
            stack.append(int(token))

    return stack[0]


# Тесты
print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
