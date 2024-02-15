input_string = input("Enter a string: ")
words = input_string.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)
    else:
        print("Word is not even")