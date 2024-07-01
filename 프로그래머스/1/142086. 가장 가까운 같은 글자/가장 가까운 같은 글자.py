def solution(s):
    answer = []
    letter_dict = {}
    
    for idx, letter in enumerate(s):
        if letter not in letter_dict:
            answer.append(-1)
            letter_dict[letter] = idx

        else:
            answer.append(idx - letter_dict[letter])
            letter_dict[letter] = idx
            
            
    return answer