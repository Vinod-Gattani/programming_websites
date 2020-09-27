# Write your MySQL query statement below

WITH cte AS (
SELECT
    a.Name, a.Salary AS "own_salary",
    b.Salary AS "manager_salary"
FROM
    Employee a
    inner join Employee b on a.ManagerId = b.Id
)

SELECT
    Name as Employee
FROM
    cte
WHERE
    own_salary > manager_salary
    
    
'''
{"headers": {"Employee": ["Id", "Name", "Salary", "ManagerId"]}, "rows": {"Employee": [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4], [3, "Sam", 60000, null], [4, "Max", 90000, null]]}}

{"headers": ["Employee"], "values": [["Joe"]]}

'''