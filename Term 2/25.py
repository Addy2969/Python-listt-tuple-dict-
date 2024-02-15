my_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
result = 1
for value in my_dict.values():
    result *= value
print("Original Dictionary:", my_dict)
print("Product of Values:", result)
