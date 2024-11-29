def solution(players, callings):
    dict_players = {player : i for i, player in enumerate(players)}
    for c in callings:
        ix = dict_players[c]
        if (ix-1 >= 0):
            tmp = players[ix-1] 
            players[ix-1] = players[ix] 
            players[ix] = tmp
            
            dict_players[tmp] = ix
            dict_players[c] = ix-1
            
        else:
            break
        
    return players