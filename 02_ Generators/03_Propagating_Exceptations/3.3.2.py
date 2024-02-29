try:
    number1 = input("Give me a number: ")
    number2 = input("Give me another number: ")
except ValueError:
    print("ValueError: No Integer was given.")
try:
    number1 / number2
except ZeroDivisionError:
    print("Division by zero is not possible.")