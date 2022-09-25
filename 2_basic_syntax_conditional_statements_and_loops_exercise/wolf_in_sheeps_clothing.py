sheeps = input()
list_of_sheeps = sheeps.split()

if list_of_sheeps[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    total_animals = len(list_of_sheeps) - 1
    index_wolf = list_of_sheeps.index('wolf,')
    if index_wolf == 0:
        print(f"Oi! Sheep number {total_animals}! You are about to be eaten by a wolf!")
    else:
        total_animals = total_animals - index_wolf
        print(f"Oi! Sheep number {total_animals}! You are about to be eaten by a wolf!")


