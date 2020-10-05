# Write your MySQL query statement below

WITH cte AS (
    SELECT
        Num,
        LEAD(num) OVER() as next_num,
        LAG(num) OVER() as prev_num
    FROM
        Logs
)

SELECT 
    DISTINCT num AS ConsecutiveNums
FROM 
    cte
WHERE
    Num = next_num and
    num = prev_num
;

'''
{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}

solution

{"headers": ["ConsecutiveNums"], "values": [[1]]}
'''