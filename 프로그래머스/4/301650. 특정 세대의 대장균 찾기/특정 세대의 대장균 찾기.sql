SELECT DISTINCT(ID)
FROM ECOLI_DATA
WHERE PARENT_ID IN
(SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN 
(SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IS NULL))
ORDER BY ID
-- 어떻게 해야 하지? 서브쿼리?