initial_items = input().split(", ")
command = ""

while command != "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        item_exist = False
        for current_item in initial_items:
            if current_item == command[1]:
                item_exist = True
                break
        if not item_exist:
            initial_items.append(command[1])
    elif command[0] == "Drop":
        for current_item in initial_items:
            if current_item == command[1]:
                initial_items.remove(current_item)
    elif command[0] == "Combine Items":
        new_list = command[1].split(":")
        for index, current_item in enumerate(initial_items):
            if current_item == new_list[0]:
                initial_items.insert(index + 1, new_list[1])
    elif command[0] == "Renew":
        initial_items.sort(key=command[1].__eq__)
    command = input()
print(', '.join(initial_items))