number_of_plants = int(input())
plants = {}
for current_plant in range(number_of_plants):
    initial_plant, rarity = input().split("<->")
    plants[initial_plant] = [int(rarity)]
command = input()
while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    plant_rating = command[1].split(" - ")
    plant = plant_rating[0]
    if plant not in plants:
        print("error")
        command = input()
        continue
    if action == "Rate":
        rating = int(plant_rating[1])
        plants[plant].append(rating)
    elif action == "Update":
        new_rarity = int(plant_rating[1])
        plants[plant][0] = new_rarity
    elif action == "Reset":
        plants[plant] = [plants[plant][0]]
    command = input()
print("Plants for the exhibition:")
for key_plant, attributes in plants.items():
    average_rating = 0
    for index, rating_value in enumerate(attributes):
        if index != 0:
            average_rating += rating_value
    if average_rating == 0:
        print(f"- {key_plant}; Rarity: {attributes[0]}; Rating: 0.00")
    else:
        print(f"- {key_plant}; Rarity: {attributes[0]}; Rating: {average_rating / (len(attributes) - 1):.2f}")

