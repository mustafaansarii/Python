# Creating a dictionary
dict_creation = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Created Dictionary:", dict_creation)

# Accessing elements
dict_access = {'name': 'John', 'age': 25, 'city': 'New York'}
name = dict_access['name']
print("Accessed Element (Name):", name)

# Iterating over keys and values
dict_iteration = {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nIterating over Dictionary:")
for key, value in dict_iteration.items():
    print(f"{key}: {value}")

# Adding a new key-value pair
dict_addition = {'name': 'John', 'age': 25, 'city': 'New York'}
dict_addition['occupation'] = 'Engineer'
print("\nDictionary after Adding a Key-Value Pair:", dict_addition)

# Updating an existing value
dict_update = {'name': 'John', 'age': 25, 'city': 'New York'}
dict_update['age'] = 26
print("Dictionary after Updating Age:", dict_update)

# Removing a key-value pair
dict_removal = {'name': 'John', 'age': 25, 'city': 'New York'}
del dict_removal['city']
print("Dictionary after Removing 'city':", dict_removal)

# Getting a list of all keys and values
dict_keys_values = {'name': 'John', 'age': 25, 'city': 'New York'}
keys = list(dict_keys_values.keys())
values = list(dict_keys_values.values())
print("\nKeys:", keys)
print("Values:", values)

# Copying a dictionary
dict_copy = {'name': 'John', 'age': 25, 'city': 'New York'}
copy_of_dict = dict_copy.copy()
print("\nCopy of Dictionary:", copy_of_dict)

# Pop an element based on a key
dict_pop = {'name': 'John', 'age': 25, 'city': 'New York'}
age = dict_pop.pop('age')
print("Popped Age:", age)
print("Dictionary after Popping 'age':", dict_pop)

# Checking if a key exists
dict_key_check = {'name': 'John', 'age': 25, 'city': 'New York'}
if 'name' in dict_key_check:
    print("\n'Name' exists in the dictionary.")

# Nested dictionaries
dict_nested = {'person': {'name': 'Alice', 'age': 30}}
print("\nNested Dictionary:", dict_nested)

