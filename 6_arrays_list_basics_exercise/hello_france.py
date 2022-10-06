initial_input = input().split("|")
separated_list = [item.split('->') for item in initial_input]
budget = float(input())

new_prices_list = []
profit = 0
total_sum = 0
for check in separated_list:
    new_price = 0
    if budget <= 0:
        continue
    if budget < float(check[1]):
        continue
    if check[0] == "Clothes":
        if float(check[1]) > 50:
            continue
        else:
            new_price += float(check[1]) * 1.4
            formatted_price = f'{new_price:.2f}'
            budget -= float(check[1])
            new_prices_list.append(formatted_price)
            profit += new_price - float(check[1])
            total_sum += new_price
    elif check[0] == "Shoes":
        if float(check[1]) > 35:
            continue
        else:
            new_price += float(check[1]) * 1.4
            formatted_price = f'{new_price:.2f}'
            budget -= float(check[1])
            new_prices_list.append(formatted_price)
            profit += new_price - float(check[1])
            total_sum += new_price
    elif check[0] == "Accessories":
        if float(check[1]) > 20.50:
            continue
        else:
            new_price += float(check[1]) * 1.4
            formatted_price = f'{new_price:.2f}'
            budget -= float(check[1])
            new_prices_list.append(formatted_price)
            profit += new_price - float(check[1])
            total_sum += new_price
print(" ".join(new_prices_list))
print(f'Profit: {profit:.2f}')
if total_sum + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
