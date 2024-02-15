string_input = input("Enter a string: ")
is_palindrome = string_input == string_input[::-1]
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")