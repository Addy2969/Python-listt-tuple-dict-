input_string = input("Enter a string: ")

unique_characters = []
for char in input_string:
    if char not in unique_characters:
        unique_characters.append(char)
result_string = ''.join(unique_characters)
print("String after removing duplicates:", result_string)