# Core calculation logic for the simple calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def tokenize(expression):
    import re
    token_pattern = re.compile(r'\d+\.?\d*|[-+*/()]')
    tokens = token_pattern.findall(expression)
    if "".join(tokens) != expression.replace(" ", ""):
        raise ValueError("Invalid characters in expression")
    return tokens

def shunting_yard(tokens):
    output_queue = []
    operator_stack = []

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.replace('.', '', 1).isdigit(): # Check if it's a number (int or float)
            output_queue.append(float(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Mismatched parentheses")
            operator_stack.pop() # Pop '('
        elif token in precedence:
            while (operator_stack and operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            raise ValueError(f"Unknown token: {token}")

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(postfix_tokens):
    operand_stack = []
    for token in postfix_tokens:
        if isinstance(token, float):
            operand_stack.append(token)
        else:
            if len(operand_stack) < 2:
                raise ValueError("Insufficient operands for operator")
            b = operand_stack.pop()
            a = operand_stack.pop()
            if token == '+':
                operand_stack.append(add(a, b))
            elif token == '-':
                operand_stack.append(subtract(a, b))
            elif token == '*':
                operand_stack.append(multiply(a, b))
            elif token == '/':
                operand_stack.append(divide(a, b))

    if len(operand_stack) != 1:
        raise ValueError("Invalid expression format")
    return operand_stack[0]

def calculate(expression):
    try:
        tokens = tokenize(expression.replace(" ", ""))
        postfix = shunting_yard(tokens)
        result = evaluate_postfix(postfix)
        return result
    except ValueError as e:
        raise e
    except Exception:
        raise ValueError("Invalid expression")

