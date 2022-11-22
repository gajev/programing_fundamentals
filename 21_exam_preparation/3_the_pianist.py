number_of_pieces = int(input())
pieces = {}
for initial_pieces in range(number_of_pieces):
    initial_piece, initial_composer, initial_key = input().split("|")
    pieces[initial_piece] = [initial_composer, initial_key]
command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    if action == "Add":
        current_composer = command[2]
        current_key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [current_composer, current_key]
            print(f"{piece} by {current_composer} in {current_key} added to the collection!")
    elif action == "Remove":
        if piece in pieces:
            print(f"Successfully removed {piece}!")
            pieces.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = command[2]
        if piece in pieces:
            print(f"Changed the key of {piece} to {new_key}!")
            pieces[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for key_piece, value_attributes in pieces.items():
    print(f"{key_piece} -> Composer: {value_attributes[0]}, Key: {value_attributes[1]}")

