# calculator.py

def add(a, b):
    # TODO: Person A
    pass

def subtract(a, b):
    # TODO: Person A
    pass

def multiply(a, b):
    # TODO: Person B
    pass

def divide(a, b):
    # TODO: Person B
    pass

def calculator():
    print("Simple Calculator (+, -, *, /)")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        num1_input = input("Enter first number: ").strip()
        if num1_input.lower() == 'q':
            break

        op = input("Enter operator (+, -, *, /): ").strip()
        if op.lower() == 'q':
            break

        num2_input = input("Enter second number: ").strip()
        if num2_input.lower() == 'q':
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Invalid number. Please enter valid decimals or integers.\n")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Use +, -, *, or /.\n")
            continue

        if result is not None:
            print(f"Result: {result:g}\n")

if __name__ == "__main__":
    calculator()