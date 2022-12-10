spices = input().split(", ")
while True:
    command = input().split()
    action = command[0]
    if action == "done":
        break
    elif action == "AddSpice":
        if not command[1] in spices:
            spices.append(command[1])
    elif action == "AddManySpices":
        index = int(command[1])
        many_spices = command[2].split("|")
        spices = spices[:index] + many_spices + spices[index:]
    elif action == "SwapSpices":
        first_spice = command[1]
        second_spice = command[2]
        if first_spice in spices and second_spice in spices:
            index_1 = spices.index(first_spice)
            index_2 = spices.index(second_spice)
            spices[index_1], spices[index_2] = spices[index_2], spices[index_1]
    elif action == "ThrowAwaySpices":
        current_spice = command[1]
        number = int(command[2])
        if current_spice in spices:
            index_current = spices.index(current_spice)
            after_index = index_current + number
            spices = spices[:index_current] + spices[after_index:]
    elif action == "Arrange":
        spices = sorted(spices)
print(" ".join(spices))