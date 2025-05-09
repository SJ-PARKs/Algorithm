-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY,PRICE) in (SELECT CATEGORY, MAX(PRICE)
                        FROM FOOD_PRODUCT
                        GROUP BY CATEGORY)
                        and CATEGORY in ('과자','국','김치','식용유')
ORDER BY PRICE DESC