from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    # terms는 여기서 분석하고 시작
    term_dict = defaultdict(str)
    for term in terms:
        alphabet, month = term.split()
        term_dict[alphabet] = int(month)
        
    # 오늘 날짜도 계산하고 시작 
    year, month, day = today.split('.')
    today_date = (int(year) * 12 * 28) + (int(month) * 28) + int(day)
    
    
    for idx, privacy in enumerate(privacies): 
        date, alphabet = privacy.split(' ') # alphabet 은 타입을 의미
        year, month, day = date.split('.')
        
        calculated_date = (int(year) * 12 * 28) + (int(month) * 28) + int(day)
        pagi_date = calculated_date + (term_dict[alphabet] * 28)
        
        # 27일 지난 것 까지는 ok, 근데 28 지난 날 땡 하면 파기해야 됨
        if pagi_date <= today_date:
            answer.append(idx + 1)
        
          
    return sorted(answer)