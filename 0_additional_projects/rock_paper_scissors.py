import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
   raise SystemExit("Invalid Input. Try again...")

if computer_move == player_move:
    print("Draw!")
elif player_move == rock and computer_move == scissors:
    print("You win!")
elif player_move == scissors and computer_move == paper:
    print("You win!")
elif player_move == paper and computer_move == rock:
    print("You win!")
else:
    print("You lose!")