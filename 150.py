# 3 ms, beats 60% :)
def evalRPN(tokens) -> int: #tokens : list[str]
    stack = []
    for t in tokens:
        if t == "+":
            stack.append(stack.pop() + stack.pop())
        elif t == "-":
            stack.append(-stack.pop() + stack.pop())
        elif t == "*":
            stack.append(stack.pop() * stack.pop())
        elif t == "/":
            stack.append(int((1 / stack.pop()) * stack.pop()))
        else:
            stack.append(int(t))
    return stack[0]

# Testing
for tokens in [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]:
    print(tokens)
    print(evalRPN(tokens))
