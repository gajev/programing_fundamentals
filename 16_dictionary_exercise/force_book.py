command = input()
dictionary = {}
while True:
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command = command.split(" | ")
        side, user = command[0], command[1]
        for check in dictionary.values():
            if user in check:
                break
        else:
            if side not in dictionary.keys():
                dictionary[side] = [user]
            else:
                dictionary[side].append(user)

    elif " -> " in command:
        command = command.split(" -> ")
        side, user = command[1], command[0]
        for key, value in dictionary.items():
            if user in value:
                dictionary[key].pop(value.index(user))
                break
        if side not in dictionary.keys():
            dictionary[side] = [user]
        else:
            dictionary[side].append(user)
        print(f"{user} joins the {side} side!")
    command = input()
for key, value in dictionary.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for current_user in value:
            print(f"! {current_user}")