string = input("Enter a string: ")
vowel = "AEIOUaeiou"
tolV = 0
for char in string:
    if char in vowel:
        tolV += 1
print("Number of vowels in the string:", tolV)
