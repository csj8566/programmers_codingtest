def solution(name, yearning, photo):
    name_yearn = dict(zip(name, yearning))
    answer = []
    
    for i in photo:
        current_sum = 0
        for j in i:
            if j in name_yearn:
                current_sum += name_yearn[j]
        answer.append(current_sum)    
    
    return answer