string_input = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
missing_vowels = vowels - set(char.lower() for char in string_input if char.isalpha())
print("Missing vowels:", missing_vowels)
