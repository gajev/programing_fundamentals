neighborhood = input().split("@")
neighborhood = [int(i) for i in neighborhood]
jump_command = input()
current_house = 0
while jump_command != "Love!":
    jump_command = jump_command.split()
    current_jump = int(jump_command[1]) + current_house
    if current_jump > len(neighborhood) - 1:
        current_jump = 0
    if neighborhood[current_jump] == 0:
        print(f"Place {current_jump} already had Valentine's day.")
        current_house = current_jump
        jump_command = input()
        continue
    else:
        neighborhood[current_jump] = neighborhood[current_jump] - 2
        if neighborhood[current_jump] == 0:
            print(f"Place {current_jump} has Valentine's day." )

    current_house = current_jump
    jump_command = input()
print(f"Cupid's last position was {current_house}.")
failure_counter = 0
for failure in neighborhood:
    if failure != 0:
        failure_counter += 1
if failure_counter > 0:
    print(f"Cupid has failed {failure_counter} places.")
else:
    print("Mission was successful.")
