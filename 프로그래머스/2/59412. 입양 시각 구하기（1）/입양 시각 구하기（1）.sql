-- 코드를 입력하세요
SELECT CASE WHEN DATE_FORMAT(DATETIME, '%H') LIKE '0%'
    THEN SUBSTRING(DATE_FORMAT(DATETIME, '%H'), 2, 1) ELSE DATE_FORMAT(DATETIME, '%H') END
    AS HOUR,
COUNT(*) AS COUNT FROM ANIMAL_OUTS
WHERE CONVERT(DATE_FORMAT(DATETIME, '%H'), SIGNED)>=9
    AND CONVERT(DATE_FORMAT(DATETIME, '%H'), SIGNED)<=19
GROUP BY (HOUR)
ORDER BY DATE_FORMAT(DATETIME, '%H');