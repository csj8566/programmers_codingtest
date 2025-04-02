def solution(lottos, win_nums):
    answer = []
    
    win_dict = {6 : 1,
                5 : 2,
                4 : 3,
                3 : 4,
                2 : 5,
                1 : 6,
                0 : 6}
    
    # 일단 초기 상태에서 lottos 와 win_nums 에 일치하는 게 몇 개 존재하는지 확인
    same_count = 0
    zero_count = 0
    for l in lottos:
        for w in win_nums:

            if l == 0:
                zero_count += 1
                break
                
            if l == w:
                same_count += 1
                break

                
    # 최대는 0 개수 만큼 더해서
    answer.append(win_dict[same_count + zero_count])
    
    # 최소는 현재 상태 그대로
    answer.append(win_dict[same_count])
    
    
    return answer



'''
둘 다 길이 엄청 짧으니까 그냥 개지랄하면서 탐색해도 됨

'''