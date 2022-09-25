import random
computer_number = random.randint(1, 100)


while True:
    player_input = (input("Guess the number 1-100: "))
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    if int(player_input) < 1 or int(player_input) > 100:
        print("Invalid input. Try again...")
        continue
    if int(player_input) == computer_number:
        print("You guessed it!")
        break
    elif int(player_input) < computer_number:
        print("Too Low!")
    else:
        print("Too High!")