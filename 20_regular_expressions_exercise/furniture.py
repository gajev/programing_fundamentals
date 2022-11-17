import re
text = input()
pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>([0]|[1-9][0-9]*)(\.\d+)?)!(?P<quantity>\d+)"
money_spent = 0
items = []
while text != "Purchase":
    matches = re.finditer(pattern, text)
    for match in matches:
        item = match.group("item")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        if item == "None" or price == "None" or quantity == "None":
            continue
        else:
            money_spent += price * quantity
            items.append(item)
    text = input()
print('Bought furniture:')
for furniture in items:
    print(furniture)
print(f'Total money spend: {money_spent:.2f}')