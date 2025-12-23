# Check if a string is palindrome
# Time: O(n)
# Space: O(n)

s = "madam"
rev = s[::-1]

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")