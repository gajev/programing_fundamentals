command = input()
pool_of_players = {}
players_skill = {}
while command != "Season end":
    if "->" in command:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in pool_of_players:
            pool_of_players[player] = [{position: skill}]
            players_skill[player] = skill
        else:
            is_position_existing = False
            skill_less = False
            for current_player in pool_of_players[player]:
                for current_position, current_skill in current_player.items():
                    if position == current_position:
                        if skill > current_skill:
                            current_player[current_position] -= current_skill
                            players_skill[player] -= current_skill
                            current_player[current_position] += skill
                            players_skill[player] += skill
                            is_position_existing = True
                            break
                        else:
                            skill_less = True
                            continue
            if not is_position_existing and not skill_less:
                pool_of_players[player].append({position: skill})
                players_skill[player] += skill
    elif "vs" in command:
        player1, player2 = command.split(" vs ")
        if player1 in pool_of_players and player2 in pool_of_players:
            for positions_player1 in pool_of_players[player1]:
                for key_player1, value_player1 in positions_player1.items():
                    for positions_player2 in pool_of_players[player2]:
                        for key_player2, value_player2 in positions_player2.items():
                            if key_player2 == key_player1:
                                if players_skill[player1] > players_skill[player2]:
                                    pool_of_players[player2].pop()
                                    players_skill.pop(player2)
                                    break
                                elif players_skill[player1] < players_skill[player2]:
                                    pool_of_players[player1].pop()
                                    players_skill.pop(player1)
                                    break
    command = input()
list_players_skill = []
for name, total_points in players_skill.items():
    list_players_skill.append([name, total_points])
ordered_list_players_skill = sorted(list_players_skill, key=lambda item: (-item[1], item[0]))
for final_player in ordered_list_players_skill:
    print(f'{final_player[0]}: {final_player[1]} skill')
    list_current_player = []
    for current_position_skill in pool_of_players[final_player[0]]:
        for current_position_to_list, current_skill_to_list in current_position_skill.items():
            list_current_player.append([current_position_to_list, current_skill_to_list])
    final_list = sorted(list_current_player, key=lambda item: (-item[1], item[0]))
    for first_list in final_list:
        print(f'- {first_list[0]} <::> {first_list[1]}')
