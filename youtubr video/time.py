import time

def example_function():
    # A simple function that performs a repetitive task
    total = 0
    for i in range(1, 10_000_000):
        total += i
    return total

# Measure execution time with time module
start_time = time.time()
result = example_function()
end_time = time.time()

execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution Time: {float(execution_time)} seconds")
