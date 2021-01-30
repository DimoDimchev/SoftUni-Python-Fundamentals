player_pool = {}

while True:
    command = input()
    if command == "Season end":
        break
    else:
        command_list = command.split()
        if len(command_list) > 3:
            command_list = command.split(" -> ")
            player = command_list[0]
            position = command_list[1]
            skill = int(command_list[2])

            if player not in player_pool:
                player_pool[player] = {}
            if position not in player_pool[player]:
                player_pool[player][position] = skill
            else:
                if player_pool[player][position] < skill:
                    player_pool[player][position] = skill
        else:
            command_list = command.split(" vs ")
            player1 = command_list[0]
            player2 = command_list[1]

            total_skill1 = 0
            total_skill2 = 0

            if player1 in player_pool and player2 in player_pool:
                for key in player_pool[player1].keys():
                    if key in player_pool[player2].keys():
                        for score in player_pool[player1].values():
                            total_skill1 += score
                        for score in player_pool[player2].values():
                            total_skill2 += score
                        if total_skill1 != total_skill2:
                            if total_skill1 > total_skill2:
                                player_pool.pop(player2)
                                break
                            else:
                                player_pool.pop(player1)
                                break

total_scores = {}
for player in player_pool:
    for position, score in player_pool[player].items():
        if player not in total_scores:
            total_scores[player] = 0
        total_scores[player] += int(score)
for player, points in sorted(total_scores.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {points} skill")
    for position, score in sorted(player_pool[player].items(), key=lambda y: (-y[1], y[0])):
        print(f"- {position} <::> {score}")
