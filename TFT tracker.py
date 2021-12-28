possibleOpponents = []
faced = []

for i in range(7):
	opp = input('enter opponents sequentially')
	possibleOpponents.append(opp)

while True:
    matchup = input('Enter the most recent opponent (type elim to remove a player):')
    if matchup == 'elim':
        eliminatedPlayer = input('Enter the name of the eliminated player:')
        if eliminatedPlayer in possibleOpponents:
            possibleOpponents.remove(eliminatedPlayer)
        if eliminatedPlayer in faced:
            faced.remove(eliminatedPlayer)

    elif matchup == 'stop':
        break

    elif matchup not in possibleOpponents or faced:
        print('Player not found.')

    else:
        if len(possibleOpponents) > 3:
            if matchup in possibleOpponents:
                possibleOpponents.remove(matchup)
                faced.append(matchup)
                print('Possible Opponents are:' + str(possibleOpponents))
            else:
                print('Player not found, enter the username correctly')
        else:
            if matchup in possibleOpponents:
                possibleOpponents.remove(matchup)
                faced.append(matchup)
                possibleOpponents.append(faced[0])
                faced.remove(faced[0])
                print('Possible Opponents are:' + str(possibleOpponents))
            else:
                print('Player not found, enter the username correctly')
