# Write your MySQL query statement below
WITH result AS (
    SELECT departmentId , name , salary,
    DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) ran
    FROM Employee
)

SELECT dp.name AS Department, result.name AS Employee, salary
FROM result
JOIN Department as dp
ON result.departmentId = dp.id
WHERE ran <= 3