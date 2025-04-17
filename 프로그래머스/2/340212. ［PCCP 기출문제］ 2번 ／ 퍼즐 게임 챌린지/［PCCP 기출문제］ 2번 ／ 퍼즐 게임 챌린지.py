def solution(diffs, times, limit):
    answer = 0
    
    left = 1
    right = max(diffs)
    
    # 이분 탐색 시작
    while left <= right: # 종료조건
        mid = (left + right) // 2 # 초기 중앙값 세팅
        # print("mid :", mid)
        temp_sum = 0
        for i in range(len(diffs)):
            if i == 0:
                temp_sum += times[0]
                # print("첫 인덱스인 경우 times[0], temp_sum:", times[0], temp_sum)
                # print()
                continue
                
            if diffs[i] <= mid:
                temp_sum += times[i]
                # print("풀 수 있음 !")
                # print("times :", times[i])
                # print("temp_sum :", temp_sum)
                # print()
                
            # (time_cur + time_prev) * (diff - level) + time_cur
            else:
                temp_sum += ((times[i] + times[i-1]) * (diffs[i] - mid) + times[i])
                # print("연마가 필요함...ㅜ")
                # print("연마 후 temp_sum :", temp_sum)
                # print()
        
        # print()
        # print("-------mid 판단 가보자고-------")
        # print()
        
        # limit 안넘겼으면 통과!
        if temp_sum <= limit:
            answer = mid
            right = mid - 1
            # print("limit 안넘겼으면 가능한 경우!")
            # print("answer :", answer)
            # print("left, right 상태 (right가 줄어듦) :", left, right)
            # print()
            
        # limit를 넘겼으면 불가능한 경우임
        # 이럴 때는 내 숙련도를 올려줘서, 틀리는 횟수를 줄여줘야 시간을 덜 걸리게 함
        else:
            answer = mid
            left = mid + 1
        #     print("limit 를 넘겨서 불가능한 경우 ㅜㅜ")
        #     print("answer :", answer)
        #     print("left, right 상태 (left가 늘어남) :", left, right)
        #     print()
        # print("-----mid 판단 끝 -----")
        # print()
   
    return left


'''
<공식>

(time_cur + time_prev) * (diff - level) + time_cur

이분 탐색!
만약 mid 로 했는데 limit 를 넘겨버린다! 이러면 result를 올려야 함
근데 limit 이하로 잘 한다! 그러면 result 내려줘도 됨
result 의 최소값을 구해야 함

종료조건?
left <= right 인 동안만!!
'''