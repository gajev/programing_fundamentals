number_of_heroes = int(input())
heroes_dict = {}
for hero in range(number_of_heroes):
    current_hero_name, hp, mp = input().split()
    heroes_dict[current_hero_name] = [int(hp), int(mp)]
command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]
    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name][1] >= mp_needed:
            heroes_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if damage >= heroes_dict[hero_name][0]:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes_dict.pop(hero_name)
        else:
            heroes_dict[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
    elif action == "Recharge":
        amount = int(command[2])
        increase = 200 - heroes_dict[hero_name][1]
        heroes_dict[hero_name][1] += amount
        if heroes_dict[hero_name][1] < 200:
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            heroes_dict[hero_name][1] = 200
            print(f'{hero_name} recharged for {increase} MP!')
    elif action == "Heal":
        heal_amount = int(command[2])
        heal_increase = 100 - heroes_dict[hero_name][0]
        heroes_dict[hero_name][0] += heal_amount
        if heroes_dict[hero_name][0] < 100:
            print(f"{hero_name} healed for {heal_amount} HP!")
        else:
            heroes_dict[hero_name][0] = 100
            print(f"{hero_name} healed for {heal_increase} HP!")
    command = input()
for current_hero, attributes in heroes_dict.items():
    print(current_hero)
    print(f"HP: {attributes[0]}")
    print(f"MP: {attributes[1]}")


