input_string = input("Enter a string: ")
half_length = len(input_string) // 2
modified_string = input_string[:half_length].upper() + input_string[half_length:]

print("Modified string:", modified_string)
