initial_list = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        current_item = command[1]
        if current_item in initial_list:
            command = input()
            continue
        else:
            current_item = command[1]
            initial_list.insert(0, current_item)
    elif command[0] == "Unnecessary":
        current_item = command[1]
        for index, check in enumerate(initial_list):
            if check == current_item:
                initial_list.pop(index)
    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        for index, check in enumerate(initial_list):
            if check == old_item:
                initial_list.pop(index)
                initial_list.insert(index, new_item)
    elif command[0] == "Rearrange":
        current_item = command[1]
        for index, check in enumerate(initial_list):
            if check == current_item:
                initial_list.pop(index)
                initial_list.append(check)
    command = input()
print(", ".join(initial_list))
