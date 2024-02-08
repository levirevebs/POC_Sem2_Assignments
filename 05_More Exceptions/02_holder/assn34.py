number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    answer = number1 / number2
    print("The answer is ",answer)
except ZeroDivisionError:
   print("Divison is not possible")
else:
    print("No value error detected")
finally:
    print("Values taken care of")
