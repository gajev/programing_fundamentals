encrypted_message = input()
command = input()
while command != "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        index = int(command[1])
        encrypted_message = encrypted_message[index:] + encrypted_message[:index]
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")
