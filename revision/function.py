# Function with parameters and return value
def add_numbers(a, b):
    result = a + b
    return result

# Function without return value
def greet(name):
    print("Hello, " + name + "!")

# Function with default parameter value
def power(base, exponent=2):
    result = base ** exponent
    return result

# Function with variable-length arguments
def sum_all(*args):
    return sum(args)

# Function with variable-length keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

# Using the functions
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)

greet("Alice")

square_result = power(4)
cube_result = power(2, 3)

print("Square:", square_result)
print("Cube:", cube_result)

total = sum_all(1, 2, 3, 4, 5)
print("Sum of all:", total)

print_info(name="John", age=30, city="New York")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5:", result)



def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

result = sum_of_natural_numbers(5)
print("Sum of first 5 natural numbers:", result)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib_result = [fibonacci(i) for i in range(8)]
print("Fibonacci Sequence:", fib_result)


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

result = power(2, 3)
print("2^3:", result)


def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_result = binary_search(sorted_array, 6, 0, len(sorted_array) - 1)
print("Binary Search Result:", search_result)
