from collections import defaultdict

def solution(gems):
    
    # 전체 gem 종류 수 구하기
    total_gems_category = len(set(gems))
    
    # gems 배열 길이
    n = len(gems)
    
    # 슬라이딩 윈도우로 해결
    start = 0
    end = 0
    
    # 최소 길이, 결과 초기화 (가장 큰 상태로)
    min_len = float('inf')
    result = [1, n] 
    
    gems_count_dict = defaultdict(int)
    
    # 슬라이딩 윈도우 진행
    while end < n: # 끝 인덱스까지 다 살펴본 경우 종료
        
        # 윈도우 확장
        gems_count_dict[gems[end]] += 1
        end += 1
        
        # 윈도우 축소
        while len(gems_count_dict) == total_gems_category:
            
            # 현재 윈도우의 길이 계산
            current_len = (end - start)
            
            if current_len < min_len:
                min_len = current_len
                result = [start+1, end] # end + 1 이 아니라 end인 이유는, end+=1 해줬기 때문
                
            gems_count_dict[gems[start]] -= 1
            
            # 만약 value가 0개가 되면 그 key를 없애줌
            if gems_count_dict[gems[start]] == 0:
                del gems_count_dict[gems[start]]
                
            start += 1
        
    
    return result