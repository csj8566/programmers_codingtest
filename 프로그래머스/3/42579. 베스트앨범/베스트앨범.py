def solution(genres, plays):
    answer = []
    genre_dict = {}
    playcount_dict = {}
    
    for idx, name in enumerate(genres):
        if name not in genre_dict:
            genre_dict[name] = 0
        if name not in playcount_dict:
            playcount_dict[name] = []
        genre_dict[name] += plays[idx]
        playcount_dict[name].append((idx, plays[idx]))
    # print(genre_dict)
    # print(playcount_dict)
    # print()
    sorted_lst = sorted(list(genre_dict.items()), key=lambda x:x[1], reverse=True)
    # print(sorted_lst)
    
    for name, playcount in sorted_lst:
        limit = 0
        playcount_dict[name].sort(key=lambda x:(-x[1], x[0]))
        answer.extend([i[0] for i in playcount_dict[name][:2]])

    return answer