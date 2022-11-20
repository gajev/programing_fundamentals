password = input()
temp_password = ""
command = input()
while command != "Done":
    command = command.split(" ")
    action = command[0]
    if action == "TakeOdd":
        for index, current_symbol in enumerate(password):
            if index % 2 != 0:
                temp_password += current_symbol
        password = temp_password
        print(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[0:index] + password[index + length:]
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            while substring in password:
                password = password.replace(substring, substitute)
                print(password)
    command = input()
print(f"Your password is: {password}")

