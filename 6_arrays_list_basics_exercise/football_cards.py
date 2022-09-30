list_of_cards = input().split()

team_a_cards = 11
team_b_cards = 11
terminated = False
new_list = []
for card in list_of_cards:
    if card in new_list:
        continue
    else:
        new_list.append(card)
    if card[0] == "A":
        team_a_cards -= 1
    elif card[0] == "B":
        team_b_cards -= 1
    if team_a_cards < 7 or team_b_cards < 7:
        terminated = True
        break

print(f"Team A - {team_a_cards}; Team B - {team_b_cards}")
if terminated:
    print("Game was terminated")