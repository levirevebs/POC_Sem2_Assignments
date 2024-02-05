def calculate_inverse(number):
    assert (number != 0), 'The number was 0!'
    return 1/number

number = int(input("Enter a number: "))
print(calculate_inverse(number))
