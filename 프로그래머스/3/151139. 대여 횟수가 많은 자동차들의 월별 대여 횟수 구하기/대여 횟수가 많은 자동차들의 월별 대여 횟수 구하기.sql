-- 코드를 입력하세요
SELECT MONTH(start_date), car_id, count(car_id) AS RECORDS FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id in (SELECT car_id FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE START_DATE BETWEEN '2022-08-01' 
                 AND '2022-10-31'
                 GROUP BY 1
                 HAVING COUNT(car_id) >= 5)
AND start_date between '2022-08-01' AND '2022-10-31'
GROUP BY 1, 2
ORDER BY 1, 2 DESC