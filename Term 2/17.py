my_list = [1, 4, 2, 7, 5, 3, 8]

sum_even_indexed = sum(my_list[i] for i in range(0, len(my_list), 2))
print("Sum of even-indexed elements:", sum_even_indexed)