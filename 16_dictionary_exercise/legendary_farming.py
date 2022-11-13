dictionary = {"shards": 0, "fragments": 0, "motes": 0}
command = input().split()
end_of_game = False
while not end_of_game:
    for index in range(0, len(command), 2):
        item = command[index + 1].lower()
        number = int(command[index])
        if item == "shards":
            dictionary["shards"] += number
            if dictionary["shards"] >= 250:
                print("Shadowmourne obtained!")
                dictionary["shards"] -= 250
                end_of_game = True
                break
        elif item == "fragments":
            dictionary["fragments"] += number
            if dictionary["fragments"] >= 250:
                print("Valanyr obtained!")
                dictionary["fragments"] -= 250
                end_of_game = True
                break
        elif item == "motes":
            dictionary["motes"] += number
            if dictionary["motes"] >= 250:
                print("Dragonwrath obtained!")
                dictionary["motes"] -= 250
                end_of_game = True
                break
        else:
            if item not in dictionary:
                dictionary[item] = 0
            dictionary[item] += number
    if end_of_game:
        break
    command = input().split()
for key, value in dictionary.items():
    print(f"{key}: {value}")
