# SELECT *
# FROM USED_GOODS_BOARD B
# RIGHT JOIN USED_GOODS_FILE F
# ON B.BOARD_ID = F.BOARD_ID
# WHERE B.VIEWS IN MAX(B.VIEWS)
# ORDER BY B.VIEWS DESC

SELECT CONCAT("/home/grep/src/", B.BOARD_ID, "/", F.FILE_ID, F.FILE_NAME, F.FILE_EXT) FILE_PATH
FROM USED_GOODS_BOARD B
RIGHT JOIN USED_GOODS_FILE F
ON B.BOARD_ID = F.BOARD_ID
WHERE B.BOARD_ID = (SELECT B.BOARD_ID
                 FROM USED_GOODS_BOARD B
                 ORDER BY VIEWS DESC
                 LIMIT 1
                 )
ORDER BY FILE_ID DESC