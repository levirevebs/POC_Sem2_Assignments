# # # def function_name(parameter1, parameter2):
# # #   #instruction1
# # #   #instruction2

# # # lambda parameter1, parameter2: #instruction

# # def sum(a, b):
# #     return a + b

# # # lambda a, b: a + b

# # # lambda x, y: x + y

# # print(sum(5, 3))

# # another_sum = lambda a, b: a + b

# # print(another_sum(5, 3))

# def apply_func(elements, func):
#     for element in elements:
#         print(func(element))


# def my_func(x): return x * x


# apply_func([1, 2, 3, 4, 5], my_func)


# def my_func(x): return 1/x


# apply_func([1, 2, 3, 4, 5], my_func)


# def my_func(x): return 0


# apply_func([1, 2, 3, 4, 5], my_func)

# apply_func([1, 2, 3, 4, 5], lambda x: x * x * x)

my_func2 = lambda x: 1 if x else 2

def printThenReturnSum(x, y):
    sum = x + y
    print(sum)
    return sum

printThenReturnSumVar = lambda x, y: printThenReturnSum(x, y)

print(printThenReturnSumVar(3, 4))

def lambda_func(i): return i * 2


initial_list = [1, 2, 3, 4, 5]


map(lambda_func, initial_list)


map_result = map(lambda_func, initial_list)
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))

map_result = map(lambda_func, initial_list)
for element in map_result:
    print(element, end=',')
    
    map_result = map(lambda_func, initial_list)
print(list(map_result))


def lambda_func(i): return i * 2


initial_list = [1, 2, 3, 4, 5]
map_result = map(lambda_func, initial_list)
print(list(map_result))

print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))

print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])))

emails = [
    'frank@gmail.com',
    'i love python',
    '98237434',
    'jonsmith@yahoo.com',
    'whereareyou@mywebsite.co.uk',
    'fs3dfss'
]
list(filter(lambda x: '@' in x, emails))


def greet(text):

    def print_greet():
        print(text)

    return print_greet


say_hello = greet('Hello')
say_hello()


def make_multiply_closure(x):

    def multiply(y):
        return x * y

    return multiply


multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))

print(multiply_12(10))
print(multiply_12(20))