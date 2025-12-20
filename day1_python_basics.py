# Day 1 - Arrays Basics (Python)

arr = [10, 20, 30, 40, 50]

# Traversing array
print("Array elements:")
for i in arr:
    print(i)

# Maximum element
max_element = arr[0]
for i in arr:
    if i > max_element:
        max_element = i

print("Maximum element:", max_element)

# Reverse array
print("Reversed array:", arr[::-1])