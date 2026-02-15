def calculate(a, b, op):
    a = int(a)
    b = int(b)
    if op == "+":
        return str(a + b)
    if op == "-":
        return str(a - b)
    if op == "*":
        return str(a * b)
    if op == "/":
        r = a // b
        if a % b != 0 and r < 0:
            return str(r + 1)
        return str(r)

# 2026-02-15 19:25 edit: 15 ms, beats 6.28% :( slow
def evalRPN(tokens) -> int: #tokens : list[str]
    operators = ["+", "-", "*", "/"]
    
    i = 0
    while i < len(tokens):
        if len(tokens) == 1:
            break
        if tokens[i] in operators:
            tokens[i - 2] = calculate(tokens[i-2], tokens[i-1], tokens[i])
            del tokens[i]
            del tokens[i - 1]
            i -= 2
        i += 1

    return int(tokens[0])

# Testing
for tokens in [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]:
    print(tokens)
    print(evalRPN(tokens))
