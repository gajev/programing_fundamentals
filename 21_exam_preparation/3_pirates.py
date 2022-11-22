command = input()
cities = {}
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]
    command = input()
new_command = input()
while new_command != "End":
    new_command = new_command.split("=>")
    event = new_command[0]
    if event == "Plunder":
        town = new_command[1]
        people = int(new_command[2])
        current_gold = int(new_command[3])
        print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= people
        cities[town][1] -= current_gold
        if cities[town][0] < 1 or cities[town][1] < 1:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    elif event == "Prosper":
        current_town = new_command[1]
        prosper_gold = int(new_command[2])
        if prosper_gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[current_town][1] += prosper_gold
            print(f"{prosper_gold} gold added to the city treasury. \
{current_town} now has {cities[current_town][1]} gold.")
    new_command = input()
if len(cities) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key_city, value_attributes in cities.items():
        print(f"{key_city} -> Population: {value_attributes[0]} citizens, Gold: {value_attributes[1]} kg")
