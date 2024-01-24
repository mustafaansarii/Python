# Creating a Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Accessing Elements
element_0 = my_tuple[0]
element_last = my_tuple[-1]
print("Accessing Elements:", element_0, element_last)

# Slicing
sub_tuple = my_tuple[1:4]
print("Slicing:", sub_tuple)

# Concatenating Tuples
tuple_2 = my_tuple + (6, 7, 8)
print("Tuple 2 (After Concatenating):", tuple_2)

# Repetition
tuple_3 = my_tuple * 2
print("Tuple 3 (After Repetition):", tuple_3)

# Length of a Tuple
length = len(my_tuple)
print("Length of Tuple:", length)

# Count Occurrences
count = my_tuple.count(4)
print("Count of 4:", count)

# Checking Membership
is_present = 3 in my_tuple
print("Is 3 present?", is_present)

# Index of an Element
index = my_tuple.index(2)
print("Index of 2:", index)

# Converting Tuple to List
tuple_as_list = list(my_tuple)
print("Tuple as List:", tuple_as_list)

# Converting List to Tuple
list_as_tuple = tuple(tuple_as_list)
print("List as Tuple:", list_as_tuple)
