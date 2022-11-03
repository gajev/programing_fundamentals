sequence_of_targets = input().split()
sequence_of_targets = [int(i) for i in sequence_of_targets]
command = input()
while command != "End":
    command = command.split()
    type_of_command = command[0]
    index = int(command[1])
    amount = int(command[2])
    if type_of_command == "Shoot":
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] = sequence_of_targets[index] - amount
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)
    elif type_of_command == "Add":
        if index < 0 or index >= len(sequence_of_targets):
            print("Invalid placement!")
        else:
            sequence_of_targets.insert(index, amount)
    elif type_of_command == "Strike":
        first_radius = index - amount
        second_radius = index + amount
        if index < 0 or index >= len(sequence_of_targets) or first_radius < 0 \
                or second_radius >= len(sequence_of_targets):
            print("Strike missed!")
        else:
            sequence_of_targets = sequence_of_targets[:first_radius] + sequence_of_targets[second_radius + 1:]
    command = input()
print(*sequence_of_targets, sep="|")