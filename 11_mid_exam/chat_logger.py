chat = []
command = input()
while command != "end":
    command = command.split()
    action = command[0]
    if action == "Chat":
        message = command[1]
        chat.append(message)
    elif action == "Delete":
        message = command[1]
        for index, element in enumerate(chat):
            if element == message:
                chat.pop(index)
    elif action == "Edit":
        message = command[1]
        for index, element in enumerate(chat):
            if element == message:
                chat[index] = command[2]
    elif action == "Pin":
        message = command[1]
        for index, element in enumerate(chat):
            if element == message:
                chat.append(message)
                chat.pop(index)
    elif action == "Spam":
        for current_message in command[1:]:
            chat.append(current_message)
    command = input()
print(*chat, sep="\n")