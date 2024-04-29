def solution(s, skip, index):
    answer = ''
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in skip:
        alphabet_list.remove(i)
    for j in s:
        try:
            answer+=alphabet_list[alphabet_list.index(j)+index]
        except:
            try:
                answer+=alphabet_list[alphabet_list.index(j)+index-len(alphabet_list)]
            except:
                answer+=alphabet_list[alphabet_list.index(j)+index-len(alphabet_list)*2]
    return answer