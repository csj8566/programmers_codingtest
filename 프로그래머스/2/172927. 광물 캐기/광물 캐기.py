def solution(picks, minerals):
    tiredness = 0
    
    dia_picks, iron_picks, stone_picks = picks
    
    dia_cost = {'diamond':1, 'iron':1, 'stone':1}
    iron_cost = {'diamond':5, 'iron':1, 'stone':1}
    stone_cost = {'diamond':25, 'iron':5, 'stone':1}
    
    minerals = [minerals[i:i+5] for i in range(0, len(minerals),5)][:sum(picks)]
    
    minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse = True)
    
    for mineral in minerals:
        if dia_picks > 0:
            for m in mineral:
                tiredness += dia_cost[m]
            dia_picks -= 1
        elif iron_picks > 0:
            for m in mineral:
                tiredness += iron_cost[m]
            iron_picks -= 1
        elif stone_picks > 0:
            for m in mineral:
                tiredness += stone_cost[m]
            stone_picks -= 1
    
    return tiredness