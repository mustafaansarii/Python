# Creating Sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
print("Set 1:", set_1)
print("Set 2:", set_2)

# Adding Elements
set_1.add(6)
print("Adding 6 to Set 1:", set_1)

# Removing Elements
set_1.remove(3)
print("Removing 3 from Set 1:", set_1)

# Discarding Elements
set_1.discard(2)
print("Discarding 2 from Set 1:", set_1)

# Pop an Element
popped_element = set_1.pop()
print("Popped Element from Set 1:", popped_element, "Updated Set 1:", set_1)

# Union of Sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7,1,2,3,48,97,2}
union_set = set_1.union(set_2)
print("Union of Set 1 and Set 2:", union_set)

# Intersection of Sets
intersection_set = set_1.intersection(set_2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference of Sets
difference_set = set_1.difference(set_2)
print("Difference of Set 1 and Set 2:", difference_set)

# Symmetric Difference of Sets
symmetric_difference_set = set_1.symmetric_difference(set_2)
print("Symmetric Difference of Set 1 and Set 2:", symmetric_difference_set)

# Subset and Superset
is_subset = set_1.issubset(set_2)
is_superset = set_1.issuperset(set_2)
print("Is Set 1 a Subset of Set 2?", is_subset)
print("Is Set 1 a Superset of Set 2?", is_superset)

# Checking Disjoint Sets
is_disjoint = set_1.isdisjoint(set_2)
print("Are Set 1 and Set 2 Disjoint?", is_disjoint)

# Copying a Set
copied_set = set_1.copy()
print("Copied Set:", copied_set)

# Clearing a Set
set_1.clear()
print("Cleared Set 1:", set_1)
