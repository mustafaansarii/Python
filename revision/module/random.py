import random

# Generate a random float between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random integer within a specific range
random_integer = random.randint(1, 10)
print("Random Integer:", random_integer)

# Generate a random floating-point number within a specific range
random_float_range = random.uniform(1.5, 4.5)
print("Random Float within Range:", random_float_range)

# Randomly shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled List:", my_list)

# Randomly choose an element from a list
random_element = random.choice(my_list)
print("Randomly Chosen Element:", random_element)

# Randomly sample elements from a list without replacement
random_sample = random.sample(my_list, 2)
print("Random Sample:", random_sample)

# Randomly choose a Boolean value
random_boolean = random.choice([True, False])
print("Random Boolean:", random_boolean)

# Seed for reproducibility
random.seed(42)
reproducible_random = random.random()
print("Reproducible Random Float:", reproducible_random)
