def orders(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    total = price * quantity
    return (f"{total:.2f}")


product = input()
quantity = int(input())
print(orders(product, quantity))