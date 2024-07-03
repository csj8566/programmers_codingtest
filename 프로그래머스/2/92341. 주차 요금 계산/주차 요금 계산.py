from math import ceil

def solution(fees, records):
    answer = []
    cars_dict = dict() # key를 차량번호로, value를 입차시간으로 갖는 딕셔너리
    time_dict = dict() # key를 차량번호로, value를 총 주차시간으로 갖는 딕셔너리
    
    for record in records:
        splited_record = record.split() # ['05:34', '5961', 'IN']
        
        if splited_record[2] == 'IN':
            time_list = splited_record[0].split(':')
            time = int(time_list[0]) * 60 + int(time_list[1]) # 334, 360, 479
            
            # 입차시간을 바꿔줌
            cars_dict[splited_record[1]] = time
            
        elif splited_record[2] == 'OUT':
            time_list = splited_record[0].split(':')
            time = int(time_list[0]) * 60 + int(time_list[1]) # 334, 360, 479
            
            if splited_record[1] not in time_dict:
                time_dict[splited_record[1]] = 0
            
            # 총주차시간에 현재시간 - 최근 입차시간만큼 더해줌
            time_dict[splited_record[1]] += time - cars_dict[splited_record[1]]
            
            # out 하지 않고 23:59 정산처리되는 차량과 그렇지 않은 차량을 구분하기 위함
            # -1 처리돼있는애는 23:59 전에 직접 정산된 애임
            cars_dict[splited_record[1]] = -1
            
    for key, value in list(cars_dict.items()):
        if value != -1:
            if key not in time_dict:
                time_dict[key] = 0
            # 23:59분 자동정산
            time_dict[key] += 1439 - value
            
    # 차량번호 기준으로 오름차순 정렬
    sorted_time = list(time_dict.items())
    sorted_time.sort(key=lambda x:x[0])
    
    for car_number, time in sorted_time:
        # 기본요금만 내도 되는 시간
        if time <= fees[0]:
            answer.append(fees[1])
            
        else:
            answer.append(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3])
    
    
    return answer