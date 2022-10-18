targets = input().split()
targets_as_int = [int(i) for i in targets]
shots_counter = 0
command = ""
while command != "End":
    if not command.isdigit():
        command = input()
        continue
    if int(command) >= len(targets_as_int):
        command = input()
        continue
    else:
        command = int(command)
        if targets_as_int[command] == -1:
            command = input()
            continue
        else:
            check_number = targets_as_int[command]
            targets_as_int[command] = -1
            shots_counter += 1
            new_list = []
            for values in targets_as_int:
                if values == -1:
                    new_list.append(values)
                    continue
                else:
                    if values > check_number:
                        values -= check_number
                        new_list.append(values)
                    elif values <= check_number:
                        values += check_number
                        new_list.append(values)
            targets_as_int = new_list
        command = input()
result = ' '.join(str(item) for item in targets_as_int)
print(f'Shot targets: {shots_counter} -> {result}')





