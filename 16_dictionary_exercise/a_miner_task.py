dictionary = {}
resource = input()
while resource != "stop":
    quantity = int(input())
    if resource in dictionary:
        dictionary[resource] += quantity
    else:
        dictionary[resource] = quantity
    resource = input()
for key, value in dictionary.items():
    print(f"{key} -> {value}")
