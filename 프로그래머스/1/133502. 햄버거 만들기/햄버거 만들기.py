def solution(ingredient):
    s = []  # 빈 스택 만들기
    cnt = 0
    for i in ingredient:
        s.append(i) # 스택에 재료 하나씩 쌓아줌
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4): # 맨 뒤에서 4개 없애버림 
                 s.pop()       # (빵, 야채, 고기, 빵이 쌓이는 순간 펑!)
                
    return cnt