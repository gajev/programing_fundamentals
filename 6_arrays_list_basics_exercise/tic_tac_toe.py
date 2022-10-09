row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
column_1 = [row_1[0], row_2[0], row_3[0]]
column_2 = [row_1[1], row_2[1], row_3[1]]
column_3 = [row_1[2], row_2[2], row_3[2]]
diagonal_1 = [row_1[0], row_2[1], row_3[2]]
diagonal_2 = [row_1[2], row_2[1], row_3[0]]
player_1_counter = 0
player_2_counter = 0
for check in row_1:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in row_2:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in row_3:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in column_1:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in column_2:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in column_3:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in diagonal_1:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
player_1_counter = 0
player_2_counter = 0
for check in diagonal_2:
    if int(check) == 1:
        player_1_counter += 1
    elif int(check) == 2:
        player_2_counter += 1
    if player_1_counter == 3 or player_2_counter == 3:
        if player_1_counter > player_2_counter:
            print("First player won")
        else:
            print("Second player won")
        quit()
print("Draw!")
