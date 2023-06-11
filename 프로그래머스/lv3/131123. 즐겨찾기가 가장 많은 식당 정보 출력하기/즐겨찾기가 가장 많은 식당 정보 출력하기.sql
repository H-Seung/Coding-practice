-- 코드를 입력하세요
SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM (
    SELECT *, RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS 등수
    FROM REST_INFO I) A
WHERE 등수 = 1
ORDER BY A.FOOD_TYPE DESC, A.VIEWS DESC;