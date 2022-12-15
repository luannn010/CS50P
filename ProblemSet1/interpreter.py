def main():
    expression = input('Expression: ')

    x, operator, y = convert(expression)
    result = interpret(x, operator, y)
    print(float(result))

def convert(string):
    x, operator, y = string.split()
    x = int(x)
    y = int(y)
    return x, operator, y

def interpret(x, operator, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y


main()
