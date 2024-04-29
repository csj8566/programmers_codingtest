def solution(genres, plays):
    answer = []
    genre_plays = {genre : 0 for genre in genres}
    genre_count = {genre : 2 for genre in genres}
    song_num = [i for i in range(len(plays))]
    
    
    for idx, genre in enumerate(genres): # (0, classic)
        genre_plays[genre] += plays[idx]
    
    
    zips = list(zip(genres, plays, song_num))
    zips.sort(key=lambda x:x[1], reverse=True)
    
    dicts = list(genre_plays.items())
    dicts.sort(key=lambda x:x[1], reverse=True)
    
    for dic in dicts: # ('pop', 3100)
        for zp in zips: # ('pop', 2500, 4)
            if zp[0] == dic[0] and genre_count[zp[0]] > 0:
                answer.append(zp[2])
                genre_count[zp[0]] -= 1
                    
        
    return answer