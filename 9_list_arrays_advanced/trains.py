number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input()
while command != "End":
    command = command.split(" ")
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        train[index] += int(command[2])
    elif command[0] == "leave":
        index = int(command[1])
        train[index] -= int(command[2])
    command = input()
print(train)
