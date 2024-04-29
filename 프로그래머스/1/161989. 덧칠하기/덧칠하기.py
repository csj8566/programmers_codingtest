def solution(n, m, section):
    result = 1
    start_point = section[0] # 2 (index : 1)
    
    for idx, next_point in enumerate(section, start=1): #1,3 / 2,6
        if next_point - start_point >= m:
            result += 1
            start_point = next_point
        
    
    return result

# section 의 첫번째 원소를 롤러의 왼쪽 끝에 대고 칠해야함
# 이 때, 롤러의 범위 안에 들어온다면 다른 section 의 원소도 동시에 칠해짐
# section 의 원소를 순환하면서 이걸 체크함
# 만약 더 이상 해당 범위에 들어가지 않은 section 의 원소가 존재한다면 롤러질 횟수를 1번 추가
# 그리고나서 그 section 의 원소를 왼쪽 끝으로 잡고 과정 반복