def solution(book_time):
    book_time.sort()
    book_time = [[int(i[0][0:2]) * 60 + int(i[0][3:]), int(i[1][0:2]) * 60 + int(i[1][3:])+10] for i in book_time]
    print('book_time :', book_time)
    
    rooms = [] # 할당된 방이 몇 개인지 보여주기 위한 배열
    for book in book_time: 
        if not rooms:
            rooms.append(book)
        else:
            for idx, room in enumerate(rooms):
                if room[-1] <= book[0]:
                    rooms[idx] = room + book
                    break
            else:
                rooms.append(book)
    
    return len(rooms)