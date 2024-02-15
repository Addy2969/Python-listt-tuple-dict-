my_list = [1, 2, 3, 4, 2, 5, 2]
number_to_find = int(input("Enter a number to find in the list: "))
if number_to_find in my_list:
    occurrences = my_list.count(number_to_find)
    print(f"{number_to_find} is present {occurrences} times.")
else:
    print(f"{number_to_find} is not present in the list.")
