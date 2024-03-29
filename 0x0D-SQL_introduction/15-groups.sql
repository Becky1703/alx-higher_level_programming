-- lists the number of records with same score in the table
-- and sorts it in descending order
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
