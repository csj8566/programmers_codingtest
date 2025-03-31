# 소요시간 : 28분

from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    # terms는 여기서 분석하고 시작
    term_dict = defaultdict(str)
    for term in terms:
        alphabet, month = term.split()
        term_dict[alphabet] = int(month)
        
    print("term_dict :", term_dict)
        
    # today 날짜도 계산하고 시작 ㄱㄱ
    year, month, day = today.split('.')
    today_date = (int(year) * 12 * 28) + (int(month) * 28) + int(day)
    
    print("today_date : ", today_date)
    print("### 자 이제 시작이야 ###")
    print()
    
    
    # privacies 하나씩 돌면서 얘가 파기해야 할 건지 아닌지 확인
    for idx, privacy in enumerate(privacies): 
        date, alphabet = privacy.split(' ') # alphabet 은 타입을 의미
        year, month, day = date.split('.')
        
        # 자 이제 분리 완료
        # terms 랑 대조해 보면서 날짜 계산 해야 함
        # 날짜 계산 어떻게 해? 
        # 년도 * 12 * 28 + 월 * 28 + 일 -> 걍 이렇게 해서 비교
        
        print(f"###{idx}번째 인덱스 보는 중###")
        calculated_date = (int(year) * 12 * 28) + (int(month) * 28) + int(day)
        print("calculated_date : ", calculated_date)
        
        # terms 랑 대조해서 이제 날짜 계산
        # 파기해야 하는 날짜는 계산된 날짜 + 약관이 보장하는 기간
        pagi_date = calculated_date + (term_dict[alphabet] * 28)
        
        print("pagi_date :", pagi_date)
        
        # 만약에 파기해야하는 날이 지났다면 append
        # 근데 같은 날짜인 것까지는 괜찮음 -> 괜찮은 게 아니었다 ?!
        # 아 한 달이 지나는 날에 파기해야 되는구나
        # 27일 지난 것 까지는 ok, 근데 28 지난 날 땡 하면 파기해야 됨
        if pagi_date <= today_date:
            answer.append(idx + 1)
            print()
            print(f"#####날짜가 지났습니다 {idx}번째 인덱스를 리스트에 추가합니다##### ")
            print()
            print("answer :", answer)
        
          
    return sorted(answer)


'''
한 달은 28일

'''