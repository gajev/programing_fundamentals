pirate_ship_status = input().split(">")
pirate_ship_status = [int(i) for i in pirate_ship_status]
warship_status = input().split(">")
warship_status = [int(i) for i in warship_status]
maximum_health = int(input())
command = input()
while command != "Retire":
    command = command.split()
    if command[0] == "Fire":
        index = int(command[1])
        damage_fire = int(command[2])
        if index >= len(warship_status) or index < 0:
            command = input()
            continue
        else:
            if damage_fire >= warship_status[index]:
                print("You won! The enemy ship has sunken.")
                quit()
            else:
                warship_status[index] = warship_status[index] - damage_fire
    elif command[0] == "Defend":
        first_index = int(command[1])
        second_index = int(command[2])
        damage_defend = int(command[3])
        if first_index < 0 or first_index >= len(pirate_ship_status) or second_index < 0 \
                or second_index >= len(pirate_ship_status):
            command = input()
            continue
        else:
            for index, defence in enumerate(pirate_ship_status):
                if first_index <= index <= second_index:
                    pirate_ship_status[index] = pirate_ship_status[index] - damage_defend
                    if pirate_ship_status[index] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        quit()
    elif command[0] == "Repair":
        repair_index = int(command[1])
        health = int(command[2])
        if repair_index >= len(pirate_ship_status) or repair_index < 0:
            command = input()
            continue
        else:
            pirate_ship_status[repair_index] = pirate_ship_status[repair_index] + health
            if pirate_ship_status[repair_index] > maximum_health:
                pirate_ship_status[repair_index] = maximum_health
    elif command[0] == "Status":
        treshold = maximum_health * 0.2
        sections_for_repairing = 0
        for section in pirate_ship_status:
            if section < treshold:
                sections_for_repairing += 1
        print(f"{sections_for_repairing} sections need repair.")
    command = input()
total_pirate_status = 0
total_warship_status = 0
for status in pirate_ship_status:
    total_pirate_status += status
for status_warship in warship_status:
    total_warship_status += status_warship

print(f"Pirate ship status: {total_pirate_status}")
print(f"Warship status: {total_warship_status}")
