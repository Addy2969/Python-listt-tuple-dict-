input_string = input("Enter a string: ")

if any(char.isalpha() for char in input_string) and any(char.isdigit() for char in input_string):
    print("String has at least one letter and one number.")
else:
    print("String does not have both a letter and a number.")