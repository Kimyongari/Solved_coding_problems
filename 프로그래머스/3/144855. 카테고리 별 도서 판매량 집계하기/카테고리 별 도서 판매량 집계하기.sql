-- 코드를 입력하세요
SELECT BOOK.CATEGORY, SUM(BOOK_SALES.SALES) AS TOTAL_SALES
FROM BOOK

INNER JOIN BOOK_SALES ON (BOOK.BOOK_ID = BOOK_SALES.BOOK_ID)
WHERE BOOK_SALES.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY BOOK.CATEGORY
ORDER BY BOOK.CATEGORY