from itertools import product

def solution(users, emoticons):
    discount_rate = [10,20,30,40]
    discount_product = list(product(discount_rate, repeat=len(emoticons)))
    
    final_plus = 0
    final_payment = 0
    
    # 순열 원소별로 (할인율 종류별로)
    for discount in discount_product: # (10,10,10,10)
        current_plus = 0
        current_payment = 0
        
        # 구매자별로
        for user in users: # [40,2900]
            payment = 0
            
            # 이모티콘별로
            for idx, emoticon in enumerate(emoticons): # 0, 1300
                if user[0] <= discount[idx]:
                    payment += emoticon * ((100 - discount[idx]) / 100)
            if payment >= user[1]:
                current_plus += 1
            else:
                current_payment += payment
        
        if final_plus < current_plus:
            final_plus = current_plus
            final_payment = current_payment
            
        elif final_plus == current_plus:
            if final_payment < current_payment:
                final_payment = current_payment

    
    return [final_plus, final_payment]