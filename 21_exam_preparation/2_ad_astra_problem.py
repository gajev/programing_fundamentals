import re
text = input()
product_list = []
date_list = []
calories_list = []

pattern = r"(#|\|)(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
matches = re.finditer(pattern, text)
for match in matches:
    product = match.group("product")
    date = match.group("date")
    calories = match.group("calories")
    product_list.append(product)
    date_list.append(date)
    calories_list.append(int(calories))
total_calories = sum(calories_list)
food_for_x_days = total_calories // 2000
print(f"You have food to last you for: {food_for_x_days} days!")
for index in range(len(product_list)):
    print(f"Item: {product_list[index]}, Best before: {date_list[index]}, Nutrition: {calories_list[index]}")
