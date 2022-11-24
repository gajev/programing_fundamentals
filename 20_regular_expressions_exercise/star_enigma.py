import re
number_of_messages = int(input())
pattern = r"@(?P<planet>[A-Za-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*!(?P<type_attack>A|D)[^\@\-\!\:\>]*!->(?P<soldier_count>\d+)"
attacked_planet, destroyed_planet = [], []
for current_string in range(number_of_messages):
    message = input()
    counter = 0
    encrypted_message = ""
    for star_symbol in message:
        if star_symbol.lower() == "s" or star_symbol.lower() == "t" or \
                star_symbol.lower() == "a" or star_symbol.lower() == "r":
            counter += 1
    for encrypting in message:
        encrypted_message += chr(ord(encrypting) - counter)
    matches = re.finditer(pattern, encrypted_message)
    for match in matches:
        planet = match.group("planet")
        type_attack = match.group("type_attack")
        if type_attack == "A":
            attacked_planet.append(planet)
        elif type_attack == "D":
            destroyed_planet.append(planet)
print(f"Attacked planets: {len(attacked_planet)}")
for current_planet in sorted(attacked_planet):
    print(f"-> {current_planet}")
print(f"Destroyed planets: {len(destroyed_planet)}")
for current_planets in sorted(destroyed_planet):
    print(f"-> {current_planets}")
