n = int(input("Enter the number of elements: "))
my_list = [int(input("Enter element: ")) for _ in range(n)]
average = sum(my_list) / n
print("Average of elements:", average)
