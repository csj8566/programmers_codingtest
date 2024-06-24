from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    enemy_sum = 0
    hq = []
    
    # ----------------------------------------------
    # 무적권 개수가 enemy 원소 개수보다 많거나 같으면 len(enemy) return 해주고 끝내주셈.
    if k >= len(enemy):
        return len(enemy)
    
    # enemy 의 원소 하나씩 돌면서 
    for e in enemy:
        # 현재 가지고 있는 병사들이랑 맞짱 뜨게 하셈
        # 맞짱 뜨고나면 현재 가지고 있는 병사들은, 현재라운드의 적군 수만큼 줄어듦
        # 이걸 적군의 총 공세를 계속 더해주는 식으로 구현
        enemy_sum += e
        heappush(hq, -e)
        
        # 남은 병사 수 < 현재 라운드의 적의 수
        if n < enemy_sum:
            # 수틀렸노; 무적권 썼어야 했네.
            if k > 0: # 무적권 남아있었을 때
                temp = heappop(hq) # 가장 인원수 많은 적을 무적권을 통해서 상대했다 치자.
                enemy_sum += temp # temp 가 음수니까 덧셈.
                k -= 1
            else:
                return answer 
            
        # 그리고 스테이지 하나 클리어.
        answer += 1
    
    

    
    
    
    # 몇 라운드까지 막아낼 수 있는지 알려주셈
    # 모든 라운드를 막을 수 있는 경우 len(enemy[i]) return 해주셈
    return answer