my_list = [6, 9, 7, 1, 4, 2 , 9]

even_numbers = [num for num in my_list if num % 2 == 0]

if even_numbers:
    largest_even = max(even_numbers)
    print("Largest even number:", largest_even)
else:
    print("Even not found in the list.")