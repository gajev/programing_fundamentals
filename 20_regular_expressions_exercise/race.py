
list_of_participants = input().split(", ")
dict_of_participants = {}

command = input()
while command != "end of race":
    name_participant = ""
    distance = 0
    for symbol in command:
        if symbol.isalpha():
            name_participant += symbol
        elif symbol.isdigit():
            distance += int(symbol)
    if name_participant in list_of_participants:
        if name_participant in dict_of_participants:
            dict_of_participants[name_participant] += distance
        else:
            dict_of_participants[name_participant] = distance
    command = input()
dict_for_print = sorted(dict_of_participants.items(), key=lambda x: x[1], reverse=True)
for index, racer in enumerate(dict_for_print):
    if index == 0:
        print(f"{index + 1}st place: {racer[0]}")
    elif index == 1:
        print(f"{index + 1}nd place: {racer[0]}")
    elif index == 2:
        print(f"{index + 1}rd place: {racer[0]}")


