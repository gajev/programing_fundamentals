initial_list = input().split()
command = input()
while command != "No Money":
    current_list = command.split()
    if current_list[0] == "OutOfStock":
        for i in range(len(initial_list)):
            if initial_list[i] == current_list[1]:
                initial_list[i] = "None"
    elif current_list[0] == "Required":
        if int(current_list[2]) <= len(initial_list):
            for j in range(len(initial_list)):
                if j == int(current_list[2]):
                    initial_list[j] = current_list[1]
        else:
            pass
    elif current_list[0] == "JustInCase":
        initial_list.pop()
        initial_list.append(current_list[1])
    else:
        for k in current_list:
            initial_list.append(k)
    command = input()
for remove_none in initial_list:
    if "None" in initial_list:
        initial_list.remove("None")
print(" ".join(initial_list))