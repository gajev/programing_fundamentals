key = input().split()
command = input()
while command != "find":
    final_word = ""
    index = 0
    for current_letter in command:
        if index >= len(key):
            index = 0
        final_word += chr(ord(current_letter) - int(key[index]))
        index += 1
    treasure_type = ""
    coordinates = ""
    adding_symbol = False
    adding_coordinates = False
    for index, symbol in enumerate(final_word):
        if symbol == "&":
            if adding_symbol:
                adding_symbol = False
                continue
            else:
                adding_symbol = True
                continue
        if adding_symbol:
            treasure_type += symbol
        if symbol == "<":
            if adding_coordinates:
                adding_coordinates = False
                continue
            else:
                adding_coordinates = True
                continue
        if adding_coordinates and symbol != ">":
            coordinates += symbol

    print(f"Found {treasure_type} at {coordinates}")
    command = input()
