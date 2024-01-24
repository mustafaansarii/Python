# Introduction to Loops in Python

# For Loop
print("Using For Loop:")
for i in range(5):  # This loop will iterate 5 times (0 to 4)
    print(i)

# While Loop
print("\nUsing While Loop:")
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Nested Loops
print("\nUsing Nested Loops:")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# For Loop with Conditional Statements
print("\nUsing For Loop with Conditional Statements:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Break and Continue Statement
print("\nUsing Break and Continue:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    elif i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd. Continuing to the next iteration.")
        continue

# Loops Problem Solving
print("\nLoops Problem Solving:")
# Let's find the sum of all even numbers from 1 to 10
sum_even = 0
for num in range(1, 11):
    if num % 2 == 0:
        sum_even += num

print(f"The sum of even numbers from 1 to 10 is: {sum_even}")


# while Loop:

# The while loop is used to repeatedly execute a block of code as long as the specified condition is true.
# The condition is evaluated before each iteration, and if it becomes false, the loop is terminated.
# Example of a simple while loop:
    
count = 0
while count < 5:
    print(count)
    count += 1


# while True Loop:

# The while True loop creates an infinite loop. It will continue to execute the block of code indefinitely unless a break statement is encountered or the program is interrupted externally (e.g., by the user).
# Example of a while True loop with a break statement:

while True:
    user_input = input("Enter 'exit' to end the loop: ")
    if user_input.lower() == 'exit':
        break
    else:
        print("Loop continues...")
