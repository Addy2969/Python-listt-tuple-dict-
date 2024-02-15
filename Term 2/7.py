input_string = input("Enter a string: ")
words = input_string.split()

modified_words = [word[0].capitalize() + word[1:-1] + word[-1].capitalize() for word in words]
modified_string = ' '.join(modified_words)

print("Modified string:", modified_string)