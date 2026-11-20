try:
    choice = input("Math Equation: ").strip()
    equation = choice.split()

    if len(equation) != 3:
        raise IndexError

    firstValue = int(equation[0])
    secondValue = int(equation[2])

    if equation[1] == "+":
        print(f"{firstValue} + {secondValue} = {firstValue + secondValue}")
    elif equation[1] == "-":
        print(f"{firstValue} - {secondValue} = {firstValue - secondValue}")
    elif equation[1] == "/":
        print(f"{firstValue} / {secondValue} = {firstValue / secondValue}")
    elif equation[1] == "*":
        print(f"{firstValue} * {secondValue} = {firstValue * secondValue}")
    else:
        print("Invalid operator. Use +, -, *, or /.")

except IndexError:
    print("Invalid format. Use spaces between numbers and operator (e.g., 5 + 3).")
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
except ZeroDivisionError:
    print("Can't Divide by 0")
