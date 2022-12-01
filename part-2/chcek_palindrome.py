#  Program to check if a string is palindrome

str_example = 'aIbohPhoBiA'

# make it suitable for caseless comparison
str_example = str_example.casefold()

# reverse the string
rev_str = reversed(str_example)

# check if the string is equal to its reverse
if list(str_example) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
