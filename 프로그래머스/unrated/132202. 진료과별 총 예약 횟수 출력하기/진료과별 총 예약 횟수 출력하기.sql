-- 코드를 입력하세요
SELECT MCDP_CD '진료과 코드', COUNT(*) '5월예약건수'
FROM APPOINTMENT 
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
ORDER BY 2, 1