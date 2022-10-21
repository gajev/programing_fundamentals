initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        for current_item in command[1:]:
            if current_item not in initial_loot:
                initial_loot.insert(0, current_item)
    elif action == "Drop":
        index = int(command[1])
        if index < 0 or index >= len(initial_loot):
            command = input()
            continue
        else:
            initial_loot.append(initial_loot.pop(index))
    elif action == "Steal":
        count = int(command[1])
        stolen_list = []
        if count >= len(initial_loot):
            for item in initial_loot:
                stolen_list.append(item)
            print(", ".join(stolen_list))
            initial_loot = []
        else:
            for steal in range(count):
                stolen_list.append(initial_loot[-1])
                initial_loot.pop(-1)
            stolen_list = reversed(stolen_list)
            print(", ".join(stolen_list))
    command = input()
if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    treasure_gain = 0
    for sum_of_symbols in initial_loot:
        treasure_gain += len(sum_of_symbols)
    treasure_gain = treasure_gain / len(initial_loot)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")

