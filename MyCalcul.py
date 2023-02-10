class Calculator:
    def add(x,y):
        return x + y

    def substract(x,y):
        return x - y

    def multiply(x,y):
        return x * y

    def divide(x,y):
        return x / y

    def power(x,y):
        result = 1
        for i in range(y):
            result *= x
        return result

    def square_root(x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        
        return val
    
    def calculate(operation, x, y):

        if operation == "add":
                result = Calculator.add(x,y)
        elif operation == "substract":
                result = Calculator.substract(x,y)
        elif operation == "multiply":
                result = Calculator.multiply(x,y)
        elif operation == "divide":
                result = Calculator.divide(x,y)
        elif operation == "power":
                result = Calculator.power(x,y)
        elif operation == "square_root":
                result = Calculator.square_root(x)
        return result

while True:
    operation = input("Enter the operation you would like to perform (add, substract, multiply, divide, power, square_root): ")
    valid_operations = ['add', 'substract', 'multiply', 'divide', 'power', 'square_root']
    if operation not in valid_operations:
        print("Enter a valid operation")
        continue

    if operation == 'square_root':
        try:
            num1 = int(input("Enter the first number : "))
        except ValueError:
            print("Enter a valid number")
            continue
    else:
        try:
            num1 = int(input("Enter the number : "))
        except ValueError:
            print("Enter a valid number")
            continue
        try:
            num2 = int(input("Enter the second number : "))
        except ValueError:
            print("Enter a valid number")
            continue
        break

print(Calculator.calculate(operation, num1, num2))
