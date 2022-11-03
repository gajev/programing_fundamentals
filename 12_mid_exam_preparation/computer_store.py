command = input()

price_without_taxes = 0
while command != "special" and command != "regular":
    command = float(command)
    if command < 0:
        print("Invalid price!")
    else:
        price_without_taxes += command
    command = input()
total_price = price_without_taxes * 1.2
taxes = price_without_taxes * 0.2
if command == "special":
    total_price = total_price * 0.9
if price_without_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print("-----------")
    print(f"Total price: {total_price:.2f}$")