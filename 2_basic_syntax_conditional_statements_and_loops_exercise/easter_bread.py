budget = float(input())
price_flour = float(input())
eggs_price = price_flour * 0.75
milk_price = price_flour * 1.25 * 0.25
price_per_loaf = price_flour + eggs_price + milk_price
colored_eggs_counter = 0
loaf_counter = 0

while budget >= price_per_loaf:
    budget -= price_per_loaf
    colored_eggs_counter += 3
    loaf_counter += 1
    if loaf_counter % 3 == 0:
        loss = loaf_counter - 2
        colored_eggs_counter -= loss

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")