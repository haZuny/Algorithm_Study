-- 코드를 작성해주세요
SELECT II.ITEM_ID, II.ITEM_NAME FROM ITEM_INFO AS II
JOIN ITEM_TREE AS IT ON II.ITEM_ID=IT.ITEM_ID
WHERE ISNULL(IT.PARENT_ITEM_ID)
ORDER BY II.ITEM_ID;