original_list = [2, 3, 4, 5, 6, 7, 8]
filtered_list = [original_list[i] for i in range(len(original_list)) if i not in [0, 3, 5]]

print("Original List:", original_list)
print("List after removing 0th, 3rd, and 5th elements:", filtered_list)