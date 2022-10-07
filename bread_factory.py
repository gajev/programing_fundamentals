initial_energy = 100
initial_coins = 100

events_or_ingredient = input().split("|")
separated_list_events_or_ingredient = [item.split('-') for item in events_or_ingredient]
day_completed = True

for event in separated_list_events_or_ingredient:
    if event[0] == "rest":
        current_energy = initial_energy
        initial_energy += int(event[1])
        if initial_energy > 100:
            initial_energy = 100
            gained_energy = initial_energy - current_energy
            print(f'You gained {gained_energy} energy.')
            print(f' Current energy: {initial_energy}.')
        else:
            gained_energy = int(event[1])
            print(f'You gained {gained_energy} energy.')
            print(f' Current energy: {initial_energy}.')
    elif event[0] == "order":
        if initial_energy < 30:
            initial_energy += 50
            print("You had to rest!")
            continue
        else:
            initial_energy -= 30
            gained_coins = int(event[1])
            initial_coins += gained_coins
            print(f' You earned {gained_coins} coins.')
    else:
        ingredient = event[0]
        if initial_coins >= int(event[1]):
            initial_coins -= int(event[1])

            print(f"You bought {ingredient}.")
        else:
            print(f'Closed! Cannot afford {ingredient}.')
            day_completed = False
            break
if day_completed:
    print("Day completed!")
    print(f'Coins: {initial_coins}')
    print(f' Energy: {initial_energy}')
