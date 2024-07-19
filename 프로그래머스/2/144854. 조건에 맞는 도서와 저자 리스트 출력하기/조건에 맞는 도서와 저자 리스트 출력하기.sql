SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK INNER JOIN AUTHOR 
ON BOOK.author_id = AUTHOR.author_id
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE