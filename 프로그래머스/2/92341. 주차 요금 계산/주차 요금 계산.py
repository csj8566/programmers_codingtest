from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    cars_dict = dict() # key를 차량번호로, value를 
    time_dict = dict() # key를 차량번호로, value를 시간으로 갖는 딕셔너리
    
    for record in records:
        splited_record = record.split() # ['05:34', '5961', 'IN']
        
        if splited_record[2] == 'IN':
            time_list = splited_record[0].split(':')
            time = int(time_list[0]) * 60 + int(time_list[1]) # 334, 360, 479
            
            cars_dict[splited_record[1]] = time
            
        elif splited_record[2] == 'OUT':
            time_list = splited_record[0].split(':')
            time = int(time_list[0]) * 60 + int(time_list[1]) # 334, 360, 479
            
            if splited_record[1] not in time_dict:
                time_dict[splited_record[1]] = 0
                
            time_dict[splited_record[1]] += time - cars_dict[splited_record[1]]
            cars_dict[splited_record[1]] = -1
            
    # print(cars_dict)
    for key, value in list(cars_dict.items()):
        if value != -1:
            if key not in time_dict:
                time_dict[key] = 0
            time_dict[key] += 1439 - value
            
    # print(cars_dict)
    # print(time_dict)
    
    
    sorted_time = list(time_dict.items())
    sorted_time.sort(key=lambda x:x[0])
    # print(sorted_time)
    
    for car_number, time in sorted_time:
        # 기본요금만 내도 되는 시간
        if time <= fees[0]:
            answer.append(fees[1])
            
        else:
            answer.append(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3])
    
    
    return answer


'''
- 주차요금은 나갈때마다 정산되는 게 아니라 일간 이용시간 합계에 따른 일괄계산임

스택?
딕셔너리

아 이거 23:59 에 빠져나가는거 계산이 어려워서 stack 으로 하는 게 맞는 것 같은데

굳이 딕셔너리 할 필요 없는게 결국 return 할때는 ... 아 아니네 차량번호별로 오름차순 해야 하는구나
'''