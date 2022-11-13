food_quantities_list = input().split()
bakery = {}
for index in range(0, len(food_quantities_list), 2):
    key = food_quantities_list[index]
    value = food_quantities_list[index + 1]
    bakery[key] = int(value)
print(bakery)
