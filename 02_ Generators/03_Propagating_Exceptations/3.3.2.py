number1 = input
number2 = input
try:
    input("Give me a number: ")
    input("Give me another number: ")
except ValueError:
    print("ValueError: No Integer was given.")

try:
    number1 / number2
except ZeroDivisionError:
    print("Division by zero is not possible.")