sequence_of_elements = input().split()
command = input()
moves_counter = 0

while command != "end":
    middle = len(sequence_of_elements) / 2
    moves_counter += 1
    command = command.split()
    command = [int(i) for i in command]
    first_index = command[0]
    second_index = command[1]

    if first_index == second_index or first_index < 0 or first_index >= len(sequence_of_elements) or second_index < 0 \
            or second_index >= len(sequence_of_elements):
        negative_moves_counter = moves_counter * -1
        element = str(negative_moves_counter) + "a"
        sequence_of_elements.insert(int(middle), element)
        sequence_of_elements.insert(int(middle), element)
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if sequence_of_elements[first_index] != sequence_of_elements[second_index]:
        print("Try again!")
    else:
        match = sequence_of_elements[first_index]
        print(f"Congrats! You have found matching elements - {match}!")
        sequence_of_elements.remove(match)
        sequence_of_elements.remove(match)
    if len(sequence_of_elements) == 0:
        break
    command = input()
if len(sequence_of_elements) == 0:
    print(f"You have won in {moves_counter} turns!")
else:

    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))

