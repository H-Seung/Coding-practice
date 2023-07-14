# SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
# FROM MEMBER_PROFILE M
# RIGHT JOIN REST_REVIEW R 
# ON M.MEMBER_ID = R.MEMBER_ID
# WHERE M.MEMBER_ID IN ( -- 최대 리뷰수를 가진 멤버ID 추출
#     SELECT M.MEMBER_ID FROM MEMBER_PROFILE M
#     RIGHT JOIN REST_REVIEW R ON M.MEMBER_ID = R.MEMBER_ID
#     GROUP BY R.MEMBER_ID
#     HAVING COUNT(R.REVIEW_ID) = ( -- 최대 개수 추출
#         SELECT COUNT(R.REVIEW_ID)
#         FROM REST_REVIEW R
#         GROUP BY R.MEMBER_ID
#         ORDER BY 1 DESC
#         LIMIT 1
#         )
#     )
# ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT











-- 두 번째 풀이 9:20 ~  32-47 ~ 19--
# SELECT *, COUNT(R.MEMBER_ID)
# # , M.MEMBER_NAME, R.REVIEW_TEXT, R.REVIEW_DATE
# FROM REST_REVIEW R
# JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
# WHERE COUNT(M.MEMBER_ID) = (
#                         SELECT COUNT(R.MEMBER_ID)
#                         FROM REST_REVIEW R
#                         GROUP BY R.MEMBER_ID
#                         ORDER BY 1 DESC
#                         LIMIT 1)
# ORDER BY R.REVIEW_DATE

SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM REST_REVIEW R
JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
WHERE M.MEMBER_ID IN (
                    SELECT R.MEMBER_ID
                    FROM REST_REVIEW R
                    GROUP BY R.MEMBER_ID
                    HAVING COUNT(M.MEMBER_ID) = (
                                        SELECT MAX(mycount)
                                        FROM (SELECT COUNT(R.MEMBER_ID) mycount
                                             FROM REST_REVIEW R
                                             GROUP BY R.MEMBER_ID) result)
                        )
ORDER BY R.REVIEW_DATE
