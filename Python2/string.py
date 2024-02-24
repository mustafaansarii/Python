# 1. Concatenation: Combining two or more strings.
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# 2. Length: Finding the length of a string.
str1 = "Hello"
length = len(str1)
print(length)  # Output: 5

# 3. Indexing: Accessing individual characters in a string.
str1 = "Hello"
print(str1[0])  # Output: H

# 4. Slicing: Extracting a substring from a string.
str1 = "Hello World"
print(str1[0:5])  # Output: Hello

# 5. Upper and Lower Case: Converting a string to upper or lower case.
str1 = "Hello"
upper_case = str1.upper()
lower_case = str1.lower()
print(upper_case)  # Output: HELLO
print(lower_case)  # Output: hello

# 6. Strip: Removing leading and trailing whitespaces.
str1 = "  Hello World  "
stripped_str = str1.strip()
print(stripped_str)  # Output: Hello World

# 7. Split: Splitting a string into a list of substrings based on a delimiter.

str1 = "Hello,World"
split_str = str1.split(",")
print(split_str)  # Output: ['Hello', 'World']

# 8. Join: Joining a list of strings into one string using a delimiter.
list_of_strings = ['Hello', 'World']
delimiter = " "
joined_str = delimiter.join(list_of_strings)
print(joined_str)  # Output: Hello World

# 9. Replace: Replacing occurrences of a substring within a string.
str1 = "Hello World"
new_str = str1.replace("World", "Universe")
print(new_str)  # Output: Hello Universe

# 10. Find: Finding the first occurrence of a substring within a string.
str1 = "Hello World"
index = str1.find("World")
print(index)  # Output: 6
