initial_list = input().split()
temporary_list = []

command = input()
while command != "No Money":

    current_list = command.split()
    if current_list[0] == "OutOfStock":
        for i in initial_list:
            if current_list[1] == i:
                initial_list.remove(i)
    elif current_list[0] == "Required":
        if int(current_list[2]) <= len(initial_list):
            index = int(current_list[-1])
            gift_to_remove = initial_list[index]
            for j in initial_list:
                if gift_to_remove == j:
                    initial_list.remove(j)
                    initial_list.insert(1, current_list[1])
    elif current_list[0] == "JustInCase":
        initial_list.pop()
        initial_list.append(current_list[1])
    else:
        for k in current_list:
            initial_list.append(k)
    command = input()
print(initial_list)






