encrypted_message = input()
command = input()
while command != "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        number_of_letters = int(command[1])
        new_string = ""
        counter = 0
        for current_move in encrypted_message:
            counter += 1
            if counter > number_of_letters:
                break
            new_string += current_move
        encrypted_message = encrypted_message[number_of_letters:] + new_string
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        temp_string = ""
        substring = command[1]
        replacement = command[2]
        for current_change in encrypted_message:
            if current_change == substring:
                temp_string += replacement
            else:
                temp_string += current_change
        encrypted_message = temp_string
    command = input()
print(f"The decrypted message is: {encrypted_message}")