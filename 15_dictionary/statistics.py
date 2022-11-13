command = input()
product_dictionary = {}
while command != "statistics":
    key, value = command.split(": ")
    if key in product_dictionary:
        product_dictionary[key] += int(value)
    else:
        product_dictionary[key] = int(value)
    command = input()
print("Products in stock:")
for key, value in product_dictionary.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(product_dictionary)}')
print(f'Total Quantity: {sum(product_dictionary.values())}')

