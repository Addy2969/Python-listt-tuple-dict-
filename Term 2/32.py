data_list = [{'item': 'item1', 'amount': 400},
             {'item': 'item2', 'amount': 300},
             {'item': 'item1', 'amount': 750}]


combined_values = {}

for data in data_list:
    item = data['item']
    amount = data['amount']
    
    if item in combined_values:
        combined_values[item] += amount
    else:
        combined_values[item] = amount

print("Original List of Dictionaries:")
for data in data_list:
    print(data)

print("\nCombined Values:")
print(combined_values)