# Find length of string without len()
# Time: O(n)
# Space: O(1)

s = "python"
count = 0

for ch in s:
    count += 1

print("Length of string:", count)