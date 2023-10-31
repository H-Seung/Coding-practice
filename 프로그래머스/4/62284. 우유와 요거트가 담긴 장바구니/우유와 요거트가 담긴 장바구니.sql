SELECT DISTINCT(A.CART_ID)
FROM CART_PRODUCTS A
JOIN (SELECT *
     FROM CART_PRODUCTS
     WHERE NAME = 'Yogurt') B ON A.CART_ID = B.CART_ID
WHERE A.NAME = 'Milk'
ORDER BY 1
     


# # SELECT *
# # , COUNT(CART_ID)
# # FROM CART_PRODUCTS
# # WHERE NAME = 'Milk' OR NAME = 'Yogurt'
# # GROUP BY CART_ID
# # HAVING COUNT(CART_ID) > 1
# # ORDER BY CART_ID

# SELECT DISTINCT(A.CART_ID)
# FROM CART_PRODUCTS A
# JOIN (SELECT CART_ID
#      FROM CART_PRODUCTS
#      WHERE NAME = 'Yogurt') B
# ON A.CART_ID = B.CART_ID
# WHERE NAME = 'Milk'