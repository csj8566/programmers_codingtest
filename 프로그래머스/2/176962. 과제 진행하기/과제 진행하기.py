from collections import deque

def solution(plans):
    answer = []
    stop_stack = [] # 잠시 멈춘 과제
    current_stack = [] # 진행 중 과제
    
    plans.sort(key=lambda x:x[1])
    print('plans : {}'.format(plans))
    plans = deque(plans)
    
    i_name, i_start, i_running_time = plans.popleft() # 처음이면
    time, minutes = i_start.split(':')
    i_start = int(time) * 60 + int(minutes)
    i_running_time = int(i_running_time)
    
    while plans:
        u_name, u_start, u_running_time = plans.popleft()
        
        if isinstance(u_start, str):
            if ':' in u_start: # u_start 에 숫자가 아닌 게 껴있으면 다음 작업 실행 ex)'12:00'
                time, minutes = u_start.split(':')
                u_start = int(time) * 60 + int(minutes)
        u_running_time = int(u_running_time)

        
        if i_start + i_running_time > u_start: # 중도에 종료해야 하는 경우
            stop_stack.append([i_name, i_running_time - (u_start - i_start)]) # ['music', 30]
            i_name, i_start, i_running_time = u_name, u_start, u_running_time

            
        elif i_start + i_running_time == u_start: # i가 끝나는 시간과 u가 시작하는 시간이 딱 맞물리는 경우
            answer.append(i_name)
            i_name, i_start, i_running_time = u_name, u_start, u_running_time

            
        else: # i를 끝내고 u가 시작될 때까지 시간이 남는 경우 -> stop_stack 을 다뤄야함
            # science(i) ==temp[0] 가 760분~810분동안 진행됨 -> 840분까지 30분이 남음 history(u) 가 시작되기전 30분여유
            # computer(temp)를 i_name으로 바꿔주고 i_start는 science의 i_start + i_running_time (810)
            # ,i_running_time은 temp[1]가 됨
            
            
            answer.append(i_name)
            
        
            if stop_stack:
                plans.appendleft([u_name, u_start, u_running_time]) # history는 다시 되돌려놔야함
                # answer.append(i_name)
                temp = stop_stack.pop() # 가장 최근에 중지된 애 
                i_name, i_start, i_running_time = temp[0], i_start + i_running_time, temp[1] # computer, 810, 90
            # else:
            #     answer.extend(list(plans))
            #     break
            else:
                i_name, i_start, i_running_time = u_name, u_start, u_running_time

    else:
        answer.append(i_name)
        while stop_stack:
            temp = stop_stack.pop()[0]
            answer.append(temp)
        

    
    return answer