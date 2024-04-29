def solution(players, callings):
    players_dict = {player : idx for idx, player in enumerate(players)}
    for name in callings:
        temp_idx = players_dict[name] # 이게 players.index(name) 이걸 대체함
        players_dict[name] -= 1
        players_dict[players[temp_idx-1]] +=1
        
        players[temp_idx-1], players[temp_idx] = players[temp_idx], players[temp_idx-1]
    
    return players