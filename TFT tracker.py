possibleOpponents = ['agon', 'gv8', 'scarra', 'kiyoon', 'k3soju', 'robinsongz', 'kurumx']
faced = []

while True:
    matchup = input("Enter the most recent opponent:")
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
            print('Possible Opponents are:' + str(possibleOpponents))
        else:
            print('Player not found, enter the username correctly')
