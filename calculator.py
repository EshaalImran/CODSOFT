def calculator():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = input("Enter operator (+ , - , * , / ): ")

    if z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    elif z == "*":
        print(x * y)
    elif z == "/":
        print(x/y)

calculator()