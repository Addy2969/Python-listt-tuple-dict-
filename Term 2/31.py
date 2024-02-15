my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 15}

highest_3_values = sorted(my_dict.values(), reverse=True)[:3]
highest_3_pairs = {key: value for key, value in my_dict.items() if value in highest_3_values}

print("Original Dictionary:", my_dict)
print("Highest 3 values and corresponding keys:", highest_3_pairs)