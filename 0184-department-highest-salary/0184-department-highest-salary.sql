# Write your MySQL query statement below
SELECT DISTINCT d.name as Department, e.name as Employee, e.salary
FROM Employee as e
INNER JOIN Department AS d
ON e.departmentId = d.id
WHERE (e.salary , e.departmentId) IN
(
SELECT MAX(salary)  AS salary , departmentId
FROM Employee
GROUP BY departmentId
)

# where e.salary = mx.salary and e.departmentId = mx.departmentId




