# Write your MySQL query statement below



SELECT name as Customers
FROM Customers
WHERE Customers.id not in (
    SELECT customerId FROM Orders
)