original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
unique_dict = {key: value for key, value in set(original_dict.items())}

print("Original Dictionary:", original_dict)
print("Dictionary after removing duplicates:", unique_dict)