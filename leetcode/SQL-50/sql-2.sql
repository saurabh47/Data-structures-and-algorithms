-- Solution 1
SELECT name
FROM Customer
WHERE ISNULL(referee_id) OR referee_id <> 2


-- Solution 2

-- The coalesce allows you to provide a default or fallback value when NULL values are encountered in the data.

SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) <> 2