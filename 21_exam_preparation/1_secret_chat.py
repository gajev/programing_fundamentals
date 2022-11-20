concealed_message = input()
command = input()
while command != "Reveal":
    command = command.split(":|:")
    operation = command[0]
    if operation == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif operation == "Reverse":
        substring = command[1]
        if substring not in concealed_message:
            print("error")
        else:
            reverse_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += reverse_substring
            print(concealed_message)
    elif operation == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")
