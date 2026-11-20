def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

try:
  choice = input("Math Equation: ")
  equation = choice.split(" ")
  if equation[1] == "+":
    print(f"{equation[0]} + {equation[2]} = {add(int(equation[0]), int(equation[2]))}")
  if equation[1] == "-":
    print(f"{equation[0]} - {equation[2]} = {sub(int(equation[0]), int(equation[2]))}")
  if equation[1] == "/":
    print(f"{equation[0]} / {equation[2]} = {div(int(equation[0]), int(equation[2]))}")
  if equation[1] == "*":
    print(f"{equation[0]} * {equation[2]} = {mult(int(equation[0]), int(equation[2]))}")
except ZeroDivisionError:
  print("Can't Divide by 0")
