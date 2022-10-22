command = input().split("-")
to_do_list = []
while True:
    if command[0] == "End":
        break
    priority = int(command[0])
    current_task = command[1]
    to_do_list.append((priority, current_task))
    command = input().split("-")
sorted_to_do_list = [task[1] for task in sorted(to_do_list)]
print(sorted_to_do_list)

