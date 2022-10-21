initial_health = 100
initial_bitcoins = 0
dungeons_rooms = input().split("|")
best_room = 0
for room in dungeons_rooms:
    best_room += 1
    current_room = room.split()
    if current_room[0] == "potion":
        current_health = initial_health
        amount_health = int(current_room[1])
        current_health += amount_health
        if current_health >= 100:
            amount_health = 100 - initial_health
            initial_health = 100
        else:
            initial_health = current_health
        print(f"You healed for {amount_health} hp.")
        print(f"Current health: {initial_health} hp.")

    elif current_room[0] == "chest":
        amount_bitcoins = int(current_room[1])
        initial_bitcoins += amount_bitcoins
        print(f"You found {amount_bitcoins} bitcoins.")
    else:
        monster = current_room[0]
        monster_attack = int(current_room[1])
        initial_health -= monster_attack
        if initial_health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            quit()
print("You've made it!")
print(f'Bitcoins: {initial_bitcoins}')
print(f'Health: {initial_health}')



# rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000