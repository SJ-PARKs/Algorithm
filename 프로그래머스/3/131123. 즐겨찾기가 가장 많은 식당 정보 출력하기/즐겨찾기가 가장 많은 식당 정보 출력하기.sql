-- 코드를 입력하세요
WITH TEMP_TABLE AS (
    SELECT
        FOOD_TYPE,
        REST_ID,
        REST_NAME,
        FAVORITES,
        RANK() OVER(
            PARTITION BY FOOD_TYPE
            ORDER BY FAVORITES DESC
        ) AS R
    FROM 
        REST_INFO   
)

SELECT 
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM 
    TEMP_TABLE
WHERE 
    R=1
ORDER BY FOOD_TYPE DESC