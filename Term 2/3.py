input_string = input("Enter a string: ")
i = int(input("Enter the position of the character to remove: "))

if 0 <= i < len(input_string):
    modified_string = input_string[:i] + input_string[i+1:]
    print("Modified string:", modified_string)
else:
    print("Invalid position.")