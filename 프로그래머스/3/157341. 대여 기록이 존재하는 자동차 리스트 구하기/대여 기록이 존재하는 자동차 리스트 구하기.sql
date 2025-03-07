-- 코드를 입력하세요
SELECT a.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR as a JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
ON a.CAR_ID = b.CAR_ID
WHERE CAR_TYPE="세단" and YEAR(START_DATE)=2022 and MONTH(START_DATE)=10
GROUP BY CAR_ID
ORDER BY CAR_ID DESC