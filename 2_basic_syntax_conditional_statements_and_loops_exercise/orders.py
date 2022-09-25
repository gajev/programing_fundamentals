number_of_orders = int(input())
all_total_price = 0
for order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    necessary_capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if necessary_capsules < 1 or necessary_capsules > 2000:
        continue

    total_price = price_per_capsule * days * necessary_capsules
    all_total_price += total_price
    print(f'The price for the coffee is: ${total_price:.2f}')
print(f'Total: ${all_total_price:.2f}')