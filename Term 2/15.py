my_list = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6 , 0]
filtered_list = [num for num in my_list if num != 0] 
result_list = filtered_list + [0] * (len(my_list) - len(filtered_list)) 
print("Original List:", my_list)
print("List after suppressing zeros at the bottom:", result_list)