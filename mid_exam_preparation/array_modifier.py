initial_list = input().split()
command = input()

while command != "end":
    command = command.split()
    initial_list = [int(i) for i in initial_list]
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_list[index1], initial_list[index2] = initial_list[index2], initial_list[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_list[index1] = initial_list[index1] * initial_list[index2]
    elif command[0] == "decrease":
        temp_list = []
        for decrease in initial_list:
            decrease -= 1
            temp_list.append(decrease)
        initial_list = temp_list
    command = input()

print(*initial_list, sep=", ")