# Creating a List
list_1 = [1, 2, 3, 4, 5]
print("List 1:", list_1)

# Accessing Elements
element_0 = list_1[0]
element_last = list_1[-1]
print("Accessing Elements:", element_0, element_last)

# Slicing
sub_list = list_1[1:4]
print("Slicing:", sub_list)

# Appending Elements
list_2 = list_1 + [6]
print("List 2 (After Appending):", list_2)

# Inserting Elements
list_3 = list_2.copy()
list_3.insert(2, 10)
print("List 3 (After Inserting):", list_3)

# Removing Elements
list_4 = list_3.copy()
list_4.remove(3)
print("List 4 (After Removing):", list_4)

# Popping Elements
popped_element = list_4.pop(1)
print("Popped Element:", popped_element, "List 4 (After Popping):", list_4)

# Length of a List
length = len(list_4)
print("Length of List 4:", length)

# Sorting
list_5 = sorted(list_4)
print("List 5 (After Sorting):", list_5)

# Reversing
list_6 = list_5.copy()
list_6.reverse()
print("List 6 (After Reversing):", list_6)

# Concatenating Lists
list_7 = list_6 + [7, 8, 9]
print("List 7 (After Concatenating):", list_7)

# Count Occurrences
list_6=[1,2,3,4,5,4,6,7,5]
count = list_6.count(4)
print("Count of 4 in List 6:", count)

# Checking Membership
is_present = 3 in list_6
print("Is 3 present in List 6?", is_present)

# List Comprehensions
squares = [x**2 for x in list_7]
print("List of Squares (List Comprehensions):", squares)

# Clearing a List
list_8 = list_7.copy()
list_8.clear()
print("List 8 (After Clearing):", list_8)
