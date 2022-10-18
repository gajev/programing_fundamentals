energy = int(input())
command = input()
won_battle_counter = 0
while command != "End of battle":
    distance = int(command)
    if energy < distance:
        print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy")
        quit()
    else:
        energy -= distance
        won_battle_counter +=1
        if won_battle_counter % 3 == 0:
            energy += won_battle_counter
    command = input()
print(f"Won battles: {won_battle_counter}. Energy left: {energy}")
