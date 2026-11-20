try:
  choice = input("Math Equation: ")
  equation = choice.split(" ")
  
  firstValue = int(equation[0])
  secondValue = int(equation[2])
  
  if equation[1] == "+":
    print(f"{firstValue} + {secondValue} = {firstValue + secondValue}")
  if equation[1] == "-":
    print(f"{firstValue} - {secondValue} = {firstValue - secondValue}")
  if equation[1] == "/":
    print(f"{firstValue} / {secondValue} = {firstValue / secondValue}")
  if equation[1] == "*":
    print(f"{firstValue} * {secondValue} = {firstValue * secondValue}")
except ZeroDivisionError:
  print("Can't Divide by 0")
