# Day 1: Arrays (Basics)

# Creating an array (list in Python)
arr = [1, 2, 3, 4, 5]

# Traversing array
for i in arr:
    print(i)

# Insert element
arr.append(6)
print("After insert:", arr)

# Delete element
arr.remove(3)
print("After delete:", arr)

# Find max and min
print("Max:", max(arr))
print("Min:", min(arr))