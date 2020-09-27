WITH cte AS (
    
    SELECT
        Salary,
        RANK() OVER (ORDER BY Salary DESC) as salary_rank
    FROM
        Employee
)

SELECT
    MAX(CASE WHEN salary_rank=2 then Salary ELSE null END) AS SecondHighestSalary
FROM
    cte


'''
{"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}

{"headers": ["SecondHighestSalary"], "values": [[200]]}
'''