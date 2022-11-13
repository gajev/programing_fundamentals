number_of_commands = int(input())
parking = {}
for action in range(number_of_commands):
    command = input().split()
    activity = command[0]
    name = command[1]
    if activity == "register":
        plate_number = command[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {parking[name]}")
        else:
            parking[name] = plate_number
            print(f"{name} registered {parking[name]} successfully")
    elif activity == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking.pop(name)

for key, value in parking.items():
    print(f"{key} => {value}")
