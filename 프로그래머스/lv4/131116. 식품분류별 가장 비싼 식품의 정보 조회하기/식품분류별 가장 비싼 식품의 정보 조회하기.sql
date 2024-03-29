SELECT A.CATEGORY, A.PRICE MAX_PRICE, A.PRODUCT_NAME
FROM FOOD_PRODUCT A
JOIN (
    SELECT CATEGORY, MAX(PRICE) PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
) B
ON A.CATEGORY = B.CATEGORY AND A.PRICE = B.PRICE
GROUP BY A.CATEGORY
HAVING A.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY 2 DESC

