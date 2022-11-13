command = input().split()
products_dictionary = {}
while command[0] != "buy":
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in products_dictionary:
        products_dictionary[product] = [price, quantity]
    else:
        new_quantity = products_dictionary[product][1] + quantity
        products_dictionary[product] = [price, new_quantity]
    command = input().split()
for key, final_price in products_dictionary.items():
    final_price = final_price[0] * final_price[1]
    print(f"{key} -> {final_price:.2f}")
