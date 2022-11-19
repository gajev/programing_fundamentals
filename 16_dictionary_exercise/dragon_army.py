number_of_dragons = int(input())
dict_dragons = {}
for add_dragon in range(number_of_dragons):
    color_type, name, damage, health, armor = dragon = input().split()
    if not damage.isdigit():
        damage = 45
    if not health.isdigit():
        health = 250
    if not armor.isdigit():
        armor = 10
    dict_dragons[color_type] = dict_dragons.get(color_type, {})
    dict_dragons[color_type][name] = dict_dragons[color_type].get(name, [])
    (dict_dragons[color_type][name]) = [damage, health, armor]
list_dragons = []
for color, name in dict_dragons.items():
    average_damage = 0
    average_health = 0
    average_armor = 0
    for current_dragon, statistics in sorted(name.items()):
        average_damage += int(statistics[0])
        average_health += int(statistics[1])
        average_armor += int(statistics[2])
    print(f"{color}::({average_damage/len(name):.2f}/{average_health/len(name):.2f}/{average_armor/len(name):.2f})")
    for current_dragon, statistics in sorted(name.items()):
        print(f"-{current_dragon} -> damage: {int(statistics[0])}, health: {int(statistics[1])}, armor: \
{int(statistics[2])}")
