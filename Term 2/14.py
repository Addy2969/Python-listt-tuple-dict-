# Program 14
my_list = [1, 6, 7, 1, 9, 4, 2, 8, 9]
even_count = sum(1 for num in my_list if num % 2 == 0)
print("Total number of even elements:", even_count)
