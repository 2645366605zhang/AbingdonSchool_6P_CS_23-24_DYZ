def evaluateRPN(rpn: list[str]) -> int:
    stack = []
    for item in rpn:
        if item.isdigit():
            stack.append(int(item))
        elif item == "+":
            stack.append(stack[0] + stack[1])
            stack.pop(-1)
        elif item == "-":
            stack.append(stack[0] + stack[1])
            stack.pop(-1)
        elif item == "*":
            stack.append(stack[0] + stack[1])
            stack.pop(-1)
        elif item == "/":
            stack.append(stack[0] + stack[1])
            stack.pop(-1)
    return stack[0]

def evaluateRPNAlt(rpn: list[str]) -> int:
    stack = []
    for item in rpn: stack.append(int(item)) if item.isdigit() else eval(f"stack.append(stack.pop() {item} stack.pop())")
    return stack[0]

print(evaluateRPNAlt(["8", "7", "10", "+", "*"]))