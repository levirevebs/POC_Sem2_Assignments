number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number"))
except ValueError:
    print("Integer was not given.")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    number1 / number2

except 